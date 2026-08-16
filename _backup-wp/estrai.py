#!/usr/bin/env python3
"""Estrae i contenuti delle pagine WordPress in blocchi ordinati (JSON)."""
import re, json, glob, os
from html.parser import HTMLParser
from html import unescape

BASE = os.path.dirname(os.path.abspath(__file__))


class ContentParser(HTMLParser):
    """Percorre entry-content e produce blocchi ordinati: heading/paragraph/figure."""

    SKIP = {"script", "style", "noscript"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.depth_skip = 0
        self.mode = None          # 'text' | 'caption'
        self.buf = []
        self.tag_of_text = None
        self.cur_fig = None       # figure aperta

    # --- helpers -------------------------------------------------
    def _flush_text(self):
        txt = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if not txt:
            return None
        return txt

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP:
            self.depth_skip += 1
            return
        if self.depth_skip:
            return

        if tag == "figure":
            self.cur_fig = {"type": "figure", "src": None, "caption": None,
                            "w": None, "h": None}
        elif tag == "img":
            src = a.get("data-orig-file") or a.get("src") or ""
            src = src.split("?")[0]
            if "/wp-content/uploads/" in src:
                size = a.get("data-orig-size", "")
                w, h = (size.split(",") + ["", ""])[:2]
                rec = {"type": "figure", "src": os.path.basename(src),
                       "caption": None, "w": w or None, "h": h or None}
                if self.cur_fig is not None:
                    self.cur_fig.update(rec)
                else:
                    self.blocks.append(rec)
        elif tag == "figcaption":
            self.mode = "caption"
            self.buf = []
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "li"):
            self.mode = "text"
            self.tag_of_text = tag
            self.buf = []
        elif tag == "br" and self.mode:
            self.buf.append(" ")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.depth_skip = max(0, self.depth_skip - 1)
            return
        if self.depth_skip:
            return

        if tag == "figcaption":
            cap = self._flush_text()
            if self.cur_fig is not None:
                self.cur_fig["caption"] = cap
            self.mode = None
        elif tag == "figure":
            if self.cur_fig and self.cur_fig.get("src"):
                self.blocks.append(self.cur_fig)
            self.cur_fig = None
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "li") and self.mode == "text":
            txt = self._flush_text()
            if txt:
                kind = {"li": "voce"}.get(tag, "heading" if tag[0] == "h" else "paragraph")
                self.blocks.append({"type": kind, "level": tag, "text": txt})
            self.mode = None

    def handle_data(self, data):
        if self.depth_skip or not self.mode:
            return
        self.buf.append(data)


def extract_content(html):
    """Ritaglia entry-content bilanciando i div, poi lo parsa."""
    m = re.search(r'<div class="entry-content[^"]*"[^>]*>', html)
    if not m:
        return []
    i = m.end()
    depth = 1
    for tok in re.finditer(r"<(/?)div\b[^>]*>", html[i:]):
        depth += -1 if tok.group(1) else 1
        if depth == 0:
            inner = html[i:i + tok.start()]
            break
    else:
        inner = html[i:]

    p = ContentParser()
    p.feed(inner)
    return p.blocks


def title_of(html):
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return unescape(m.group(1)).split("–")[0].strip() if m else ""


def clean(blocks):
    """Toglie i residui di WordPress (share, like, navigazione)."""
    noise = re.compile(
        r"^(Mi piace|Condividi|Caricamento|Δ|document\.getElementById|"
        r"Segui|Pubblicato da|Pubblicato il|Lascia un commento|"
        r"Clicca qui per|← Precedente|Avanti →)",
        re.I)
    out = []
    for b in blocks:
        if b["type"] in ("paragraph", "heading", "voce"):
            t = b["text"]
            if not t or noise.match(t) or t.lower() in ("x", "facebook", "wordpress"):
                continue
        out.append(b)
    return out


result = {}
for f in sorted(glob.glob(os.path.join(BASE, "*.html"))):
    name = os.path.basename(f)[:-5]
    html = open(f, encoding="utf-8", errors="ignore").read()
    blocks = clean(extract_content(html))
    result[name] = {"titolo": title_of(html), "blocchi": blocks}

with open(os.path.join(BASE, "_contenuti.json"), "w", encoding="utf-8") as fh:
    json.dump(result, fh, ensure_ascii=False, indent=1)

for k, v in result.items():
    figs = sum(1 for b in v["blocchi"] if b["type"] == "figure")
    caps = sum(1 for b in v["blocchi"] if b["type"] == "figure" and b["caption"])
    print(f"{k:<70} blocchi:{len(v['blocchi']):>4}  figure:{figs:>3}  con-didascalia:{caps:>3}")
