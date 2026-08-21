#!/usr/bin/env python3
"""Trasforma i blocchi estratti nel catalogo strutturato del sito."""
import argparse, json, re, os, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# Questo script RICOSTRUISCE il catalogo dalle vecchie pagine WordPress.
# Rilanciarlo cancella le opere aggiunte in seguito con aggiungi-opera.py.
_ap = argparse.ArgumentParser(description="Re-importa il catalogo dalle pagine WordPress originali")
_ap.add_argument("--forza", action="store_true",
                 help="sovrascrive _catalogo.json anche se contiene opere aggiunte a mano")
_args = _ap.parse_args()

_esistente = os.path.join(BASE, "_catalogo.json")
if os.path.exists(_esistente) and not _args.forza:
    _vecchio = json.load(open(_esistente, encoding="utf-8"))
    _aggiunte = [o["titolo"] for o in _vecchio.get("opere", []) if o.get("n") is None]
    if _aggiunte:
        raise SystemExit(
            "Fermo: _catalogo.json contiene opere aggiunte a mano che andrebbero perse:\n"
            + "\n".join("  - " + t for t in _aggiunte)
            + "\n\nUsa --forza solo se sai cosa stai facendo (e reinserisci poi quelle opere)."
        )
d = json.load(open(os.path.join(BASE, "_contenuti.json"), encoding="utf-8"))

# --- sezioni della pagina "Le Opere" -------------------------------------
SEZIONI = {
    "la pittura": "pittura",
    "la scultura": "scultura",
    "la riproduzione dei nativi americani": "nativi",
}


def parse_didascalia(cap):
    """'3) Librarsi nel cielo, 50×40, 2020. Olio su tela.' -> campi separati."""
    cap = cap.strip()
    num = None
    m = re.match(r"^(\d+)\)\s*(.*)$", cap)
    if m:
        num, cap = int(m.group(1)), m.group(2).strip()

    # anno: 4 cifre isolate, l'ultimo che compare
    anni = re.findall(r"\b(19\d{2}|20\d{2})\b", cap)
    anno = anni[-1] if anni else None

    # misure: 80×70 / 60x50cm / 79.5×59.5 / 16,5×29,5
    mis = None
    num_re = r"\d+(?:[.,]\d+)?"
    mm = re.search(rf"\b({num_re}\s*[x×]\s*{num_re}(?:\s*[x×]\s*{num_re})?)\s*(?:cm)?", cap)
    if mm:
        mis = mm.group(1).replace(" ", "").replace("x", "×") + " cm"
    else:
        # forme discorsive: "62 cm circa", "88 cm di lunghezza"
        ms = re.search(rf"\b({num_re})\s*cm\b", cap)
        if ms:
            mis = ms.group(1) + " cm"

    # titolo: fino alla prima virgola/punto fuori dalle parentesi
    depth, taglio = 0, len(cap)
    for i, ch in enumerate(cap):
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif depth == 0 and ch == ",":
            taglio = i
            break
        elif depth == 0 and ch == "." and i + 1 < len(cap) and cap[i + 1] == " ":
            taglio = i
            break
    titolo = cap[:taglio].strip(" .,")
    titolo = re.sub(r"\.\(", " (", titolo)          # "Mato-Tope.(capo" -> "Mato-Tope (capo"
    titolo = re.sub(r"\s+([,.])", r"\1", titolo)    # spazio prima di virgola
    titolo = re.sub(r"\s{2,}", " ", titolo).strip(" .,")

    # tecnica: frase che nomina un materiale/supporto, cercata DOPO il titolo
    resto = cap[len(titolo):] if cap.lower().startswith(titolo.lower()) else cap
    tecnica = None
    for pezzo in re.split(r"[.,;]", resto):
        p = pezzo.strip(" .,")
        if not p or len(p) < 4:
            continue
        if re.search(r"\d+\s*(cm|mm|pollici|libbre)\b", p, re.I):
            continue                      # è una misura, non una tecnica
        if re.search(r"olio|terracotta|cartapesta|disegno|sanguina|china|tempera|"
                     r"acquerello|bassorilievo|altorilievo|legno|pietra|bronzo|"
                     r"scultura|pennino|faesite|iuta|tela|cartoncino|lenzuolo",
                     p, re.I):
            tecnica = p[0].upper() + p[1:]
            break

    return {"n": num, "titolo": titolo, "misure": mis, "anno": anno,
            "tecnica": tecnica, "didascalia": cap}


opere = []
sezione = None
for b in d["page-blog"]["blocchi"]:
    if b["type"] == "heading":
        sezione = SEZIONI.get(b["text"].strip().lower(), sezione)
    elif b["type"] == "figure" and b.get("caption") and sezione:
        rec = parse_didascalia(b["caption"])
        rec.update({"img": b["src"], "w": b["w"], "h": b["h"], "sezione": sezione})
        opere.append(rec)

# --- pagina "Passione per gli Indiani": schede riproduzioni ---------------
nativi = []
for b in d["page-la-passione-per-gli-indiani"]["blocchi"]:
    if b["type"] == "figure" and b.get("caption"):
        cap = re.sub(r"\s*Clicca per maggiori dettagli\.?\s*$", "", b["caption"]).strip()
        rec = parse_didascalia(cap)
        rec.update({"img": b["src"], "w": b["w"], "h": b["h"]})
        nativi.append(rec)

# --- articoli -------------------------------------------------------------
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]
articoli = []
for f in sorted(glob.glob(os.path.join(BASE, "post-*.html"))):
    slug = os.path.basename(f)[5:-5]
    html = open(f, encoding="utf-8", errors="ignore").read()
    key = os.path.basename(f)[:-5]
    blocchi = d[key]["blocchi"]

    m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    cover = os.path.basename(m.group(1).split("?")[0]) if m and "/wp-content/" in m.group(1) else None
    if not cover:
        for b in blocchi:
            if b["type"] == "figure":
                cover = b["src"]
                break

    anno, mese, giorno = slug[:4], slug[5:7], slug[8:10]
    data_it = f"{int(giorno)} {MESI[int(mese) - 1]} {anno}"

    articoli.append({
        "slug": re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug),
        "titolo": d[key]["titolo"].rstrip(". ").replace("- ", " - "),
        "data": f"{anno}-{mese}-{giorno}",
        "data_it": data_it,
        "cover": cover,
        "blocchi": blocchi,
    })
articoli.sort(key=lambda a: a["data"], reverse=True)

# --- home: biografia, rassegna stampa, mostre -----------------------------
bio, stampa, mostre, ritratto = [], [], [], None
lista_corrente = None
for b in d["page-home"]["blocchi"]:
    if b["type"] == "figure":
        if b.get("caption") and ritratto is None:
            ritratto = {"img": b["src"], "caption": b["caption"]}
    elif b["type"] == "heading":
        t = b["text"].strip().lower()
        lista_corrente = stampa if "parlano" in t else (mostre if "esibito" in t else None)
    elif b["type"] == "voce" and lista_corrente is not None:
        lista_corrente.append(b["text"])
    elif b["type"] == "paragraph":
        lista_corrente = None
        if len(b["text"]) > 80:
            bio.append(b["text"])

out = {
    "bio": bio,
    "stampa": stampa,
    "mostre": mostre,
    "ritratto": ritratto,
    "opere": opere,
    "nativi": nativi,
    "articoli": articoli,
    "tecnica": d["page-about"]["blocchi"],
    "home": d["page-home"]["blocchi"],
    "intro_nativi": [b for b in d["page-la-passione-per-gli-indiani"]["blocchi"]
                     if b["type"] == "paragraph"][:4],
}
json.dump(out, open(os.path.join(BASE, "_catalogo.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

from collections import Counter
print("OPERE per sezione:", dict(Counter(o["sezione"] for o in opere)))
print("Schede nativi:", len(nativi))
print("Articoli:", len(articoli), "| senza copertina:",
      sum(1 for a in articoli if not a["cover"]))
print()
for o in opere[:3] + opere[-3:]:
    print(f"  [{o['sezione']:<8}] {o['titolo'][:34]:<36} {str(o['misure']):<14} "
          f"{str(o['anno']):<6} {str(o['tecnica'])[:34]}")
