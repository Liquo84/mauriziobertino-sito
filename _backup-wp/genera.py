#!/usr/bin/env python3
"""Genera il sito statico di Maurizio Bertino da _catalogo.json."""
import json, os, re, shutil, html as H

BASE = os.path.dirname(os.path.abspath(__file__))
SITO = os.path.join(BASE, "..", "sito")
DOMINIO = "https://mauriziobertino.com"

# ---------------------------------------------------------------- contatti
# NOTA: sostituire i segnaposto con i recapiti reali.
CONTATTI = {
    "email": "mauriiobertinoartista@gmail.com",   # confermata da Davide: "maurii", non "maurizio"
    "whatsapp": "393314385178",        # numero personale, formato internazionale senza "+"
    "facebook": "https://www.facebook.com/mauriziobertinoartista/",
    "youtube": "https://www.youtube.com/@mauriziobertinoartista9910",
}

cat = json.load(open(os.path.join(BASE, "_catalogo.json"), encoding="utf-8"))
DIM = json.load(open(os.path.join(BASE, "_dimensioni.json"), encoding="utf-8"))


def web(nome):
    """Nome file originale -> nome della versione web (.jpg)."""
    return os.path.splitext(nome)[0] + ".jpg" if nome else None


def dim(nome):
    return DIM.get(web(nome), {"w": 800, "h": 600})


def e(t):
    return H.escape(t or "", quote=True)


# ---------------------------------------------------------------- guscio
PAGINE = [
    ("index.html", "Home"),
    ("opere.html", "Opere"),
    ("tecnica.html", "La tecnica"),
    ("nativi.html", "Nativi d’America"),
    ("diario.html", "Diario"),
    ("contatti.html", "Contatti"),
]


def nav(attiva, su=""):
    voci = []
    for f, etichetta in PAGINE:
        corrente = ' aria-current="page"' if f == attiva else ""
        voci.append(f'<a href="{su}{f}"{corrente}>{etichetta}</a>')
    return "\n        ".join(voci)


ICONA_TEMA = (
    '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" '
    'stroke-width="1.8" stroke-linecap="round" aria-hidden="true">'
    '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>'
)
ICONA_MENU = (
    '<svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" '
    'stroke-width="1.8" stroke-linecap="round" aria-hidden="true">'
    '<path d="M4 7h16M4 12h16M4 17h16"/></svg>'
)


def pagina(nome_file, titolo, descrizione, corpo, su="", og=None, classe_corpo=""):
    og_img = f"{DOMINIO}/img/full/{web(og)}" if og else f"{DOMINIO}/img/full/{web(EROE)}"
    url = f"{DOMINIO}/{'' if nome_file == 'index.html' else nome_file}"
    doc = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titolo)}</title>
<meta name="description" content="{e(descrizione)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="Maurizio Bertino">
<meta property="og:title" content="{e(titolo)}">
<meta property="og:description" content="{e(descrizione)}">
<meta property="og:image" content="{og_img}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#faf7f2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#131110" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{su}img/favicon.png">
<link rel="apple-touch-icon" href="{su}img/favicon.png">
<link rel="stylesheet" href="{su}assets/stile.css">
<noscript><style>.appare{{opacity:1;transform:none}}</style></noscript>
</head>
<body{f' class="{classe_corpo}"' if classe_corpo else ""}>

<header class="testata">
  <div class="contenitore">
    <a class="marchio" href="{su}index.html">Maurizio <span>Bertino</span></a>
    <button class="menu-btn" aria-label="Apri il menu" aria-expanded="false">{ICONA_MENU}</button>
    <nav class="menu">
        {nav(nome_file, su)}
        <button class="tema-btn" aria-label="Cambia tema chiaro/scuro">{ICONA_TEMA}</button>
    </nav>
  </div>
</header>

<main>
{corpo}
</main>

<footer class="piede">
  <div class="contenitore">
    <p>© {ANNO} Maurizio Bertino — Tutte le opere sono protette da copyright.</p>
    <nav>
      <a href="{su}opere.html">Opere</a>
      <a href="{su}nativi.html">Nativi d’America</a>
      <a href="{su}diario.html">Diario</a>
      <a href="{su}contatti.html">Contatti</a>
    </nav>
  </div>
</footer>

<div class="lente" role="dialog" aria-modal="true" aria-label="Immagine ingrandita">
  <button class="chiudi" aria-label="Chiudi">&times;</button>
  <button class="prec" aria-label="Immagine precedente">&#8249;</button>
  <button class="succ" aria-label="Immagine successiva">&#8250;</button>
  <figure><img alt=""><figcaption></figcaption></figure>
</div>

<script src="{su}assets/sito.js" defer></script>
</body>
</html>
"""
    percorso = os.path.join(SITO, nome_file)
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    open(percorso, "w", encoding="utf-8").write(doc)


ANNO = 2026
EROE = "paesaggio-albero-2018.jpg"


# ---------------------------------------------------------------- pezzi
def riga_dati(o):
    pezzi = [p for p in (o.get("misure"), o.get("anno")) if p]
    if o.get("tecnica"):
        pezzi.append(o["tecnica"])
    return " · ".join(pezzi)


def tessera_opera(o, su=""):
    d = dim(o["img"])
    dati = riga_dati(o)
    return f"""<button class="opera" data-sezione="{o.get('sezione','')}"
   data-grande="{su}img/full/{web(o['img'])}"
   data-titolo="{e(o['titolo'])}" data-dati="{e(dati)}">
  <figure style="margin:0">
    <span class="cornice"><img src="{su}img/thumb/{web(o['img'])}" width="{d['w']}" height="{d['h']}"
      loading="lazy" decoding="async" alt="{e(o['titolo'])}"></span>
    <figcaption>
      <span class="titolo">{e(o['titolo'])}</span>
      {f'<span class="dati">{e(dati)}</span>' if dati else ''}
    </figcaption>
  </figure>
</button>"""


def blocchi_html(blocchi, su=""):
    """Rende i blocchi di un articolo (paragrafi, titoli, figure, elenchi)."""
    out, in_lista = [], False
    for b in blocchi:
        if b["type"] == "voce":
            if not in_lista:
                out.append("<ul>")
                in_lista = True
            out.append(f"<li>{e(b['text'])}</li>")
            continue
        if in_lista:
            out.append("</ul>")
            in_lista = False

        if b["type"] == "paragraph":
            out.append(f"<p>{e(b['text'])}</p>")
        elif b["type"] == "heading":
            out.append(f"<h2>{e(b['text'])}</h2>")
        elif b["type"] == "figure":
            d = dim(b["src"])
            cap = b.get("caption")
            out.append(
                f'<figure><img src="{su}img/full/{web(b["src"])}" width="{d["w"]}" height="{d["h"]}"'
                f' loading="lazy" decoding="async" alt="{e(cap or "Opera di Maurizio Bertino")}"'
                f' data-grande="{su}img/full/{web(b["src"])}" data-titolo="{e(cap or "")}" data-dati="">'
                + (f"<figcaption>{e(cap)}</figcaption>" if cap else "")
                + "</figure>"
            )
    if in_lista:
        out.append("</ul>")
    return "\n".join(out)


def estratto(art, n=190):
    for b in art["blocchi"]:
        if b["type"] == "paragraph" and len(b["text"]) > 60:
            t = b["text"]
            return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"
    return ""


# ---------------------------------------------------------------- HOME
op = cat["opere"]
per_sezione = {s: [o for o in op if o["sezione"] == s] for s in ("pittura", "scultura", "nativi")}
d_eroe = dim(EROE)

porte = ""
for chiave, titolo, testo, dest in [
    ("pittura", "La pittura", "Paesaggi di fantasia, animali e nature morte. Olio su tela, iuta, faesite.", "opere.html#pittura"),
    ("scultura", "La scultura", "Terracotta, cartapesta e pietra leccese. Bassorilievo e altorilievo su vari materiali.", "opere.html#scultura"),
    ("nativi", "Nativi d’America", "Manufatti dei nativi americani, riprodotti e personalizzati nel dettaglio.", "nativi.html"),
]:
    campione = per_sezione[chiave][0] if per_sezione.get(chiave) else None
    if not campione:
        continue
    d = dim(campione["img"])
    porte += f"""
      <a class="porta appare" href="{dest}">
        <span class="scatto"><img src="img/thumb/{web(campione['img'])}" width="{d['w']}" height="{d['h']}"
          loading="lazy" decoding="async" alt="{e(titolo)}"></span>
        <span class="testo">
          <h3>{titolo}</h3>
          <p>{testo}</p>
          <span class="freccia">Guarda le opere &rarr;</span>
        </span>
      </a>"""

def figura_ritratto(nome_img, testo):
    if not nome_img:
        return ""
    d = dim(nome_img)
    return f"""
      <figure class="ritratto appare">
        <img src="img/thumb/{web(nome_img)}" width="{d['w']}" height="{d['h']}"
          loading="lazy" decoding="async" alt="{e(testo)}"
          data-grande="img/full/{web(nome_img)}" data-titolo="{e(testo)}" data-dati="">
        <figcaption>{e(testo)}</figcaption>
      </figure>"""


# ritratto in bottega (era l'immagine di anteprima social del vecchio sito)
AL_LAVORO = "5d44b1d0-1d44-4d58-a943-c387314a04ac.jpg"
blocco_ritratto = figura_ritratto(AL_LAVORO, "Maurizio Bertino al lavoro su un gufo in terracotta.")

rit = cat.get("ritratto")
blocco_stand = figura_ritratto(rit["img"], rit["caption"]) if rit else ""

bio_html = "\n".join(f"<p>{e(p)}</p>" for p in cat["bio"][:2])
bio_resto = "\n".join(f"<p>{e(p)}</p>" for p in cat["bio"][2:])

corpo_home = f"""
<section class="copertina">
  <img src="img/copertina.jpg" width="1600" height="1142"
    fetchpriority="high" decoding="async" alt="Dipinto a olio di Maurizio Bertino: un grande albero su una collina e un viandante lungo il sentiero">
  <div class="contenitore">
    <p class="sopratitolo">Pittore e scultore · Salento</p>
    <h1>Maurizio Bertino</h1>
    <p>Un’arte espressionista e non accademica. Ogni opera nasce da un’emozione
       e resta irripetibile: crea solo per chi cerca il pezzo unico.</p>
  </div>
</section>

<section class="sezione">
  <div class="contenitore">
    <div class="biografia">
      <div>
        <p class="occhiello">In breve</p>
        <h2>Uniche, per forza di cose</h2>
        {bio_html}
      </div>
      {blocco_ritratto}
    </div>
  </div>
</section>

<section class="sezione alt">
  <div class="contenitore">
    <p class="occhiello">Il lavoro</p>
    <h2>Tre sentimenti, una sola mano</h2>
    <p class="guida">Pittura, scultura e la riproduzione degli oggetti dei nativi
       nordamericani: tre modi diversi di inseguire la stessa emozione.</p>
    <div class="porte">{porte}
    </div>
  </div>
</section>

<section class="sezione">
  <div class="contenitore">
    <div class="biografia">
      <div>
        <p class="occhiello">Il percorso</p>
        <h2>Da autodidatta</h2>
        {bio_resto}
      </div>
      {blocco_stand}
    </div>
  </div>
</section>

<section class="sezione alt">
  <div class="contenitore stretto">
    <p class="occhiello">Riconoscimenti</p>
    <h2>Documentazione artistica</h2>
    <div class="due-colonne">
      <div>
        <h3>Parlano di lui</h3>
        <ul class="lista-pulita">
          {''.join(f'<li>{e(v)}</li>' for v in cat['stampa'])}
        </ul>
      </div>
      <div>
        <h3>Esposto a</h3>
        <ul class="lista-pulita">
          {''.join(f'<li>{e(v)}</li>' for v in cat['mostre'])}
        </ul>
      </div>
    </div>
  </div>
</section>
"""
pagina("index.html", "Maurizio Bertino — Pittore e scultore salentino",
       "Le opere di Maurizio Bertino: dipinti a olio, sculture in terracotta, cartapesta "
       "e pietra leccese, manufatti dei nativi d’America. Un’arte espressionista e non accademica.",
       corpo_home, og=EROE)


# ---------------------------------------------------------------- OPERE
def gruppo(chiave, titolo, intro):
    tessere = "\n".join(tessera_opera(o) for o in per_sezione[chiave])
    return f"""
<section class="sezione" id="{chiave}">
  <div class="contenitore">
    <p class="occhiello">{len(per_sezione[chiave])} opere</p>
    <h2>{titolo}</h2>
    <p class="guida">{intro}</p>
    <div class="galleria" style="margin-top:36px">
{tessere}
    </div>
  </div>
</section>"""

filtri = """
<div class="contenitore">
  <div class="filtri">
    <button class="filtro" data-filtro="tutte" aria-pressed="true">Tutte</button>
    <button class="filtro" data-filtro="pittura" aria-pressed="false">Pittura</button>
    <button class="filtro" data-filtro="scultura" aria-pressed="false">Scultura</button>
    <button class="filtro" data-filtro="nativi" aria-pressed="false">Nativi d’America</button>
  </div>
</div>"""

tutte = "\n".join(tessera_opera(o) for o in op)
corpo_opere = f"""
<section class="intestazione-pagina">
  <div class="contenitore">
    <p class="occhiello">Catalogo</p>
    <h1>Le opere</h1>
    <p class="guida">{len(op)} opere tra dipinti, sculture e riproduzioni.
       Tocca un’immagine per ingrandirla; con le frecce scorri tutta la raccolta.</p>
  </div>
</section>
{filtri}
<section class="sezione" style="padding-top:0">
  <div class="contenitore">
    <div class="galleria">
{tutte}
    </div>
  </div>
</section>
"""
pagina("opere.html", "Le opere — Maurizio Bertino",
       f"Il catalogo completo di Maurizio Bertino: {len(per_sezione['pittura'])} dipinti, "
       f"{len(per_sezione['scultura'])} sculture e {len(per_sezione['nativi'])} riproduzioni native.",
       corpo_opere, og=op[1]["img"] if len(op) > 1 else EROE)


# ---------------------------------------------------------------- TECNICA
tec = [b for b in cat["tecnica"] if b["type"] in ("paragraph", "heading", "voce")]
cita = next((b["text"] for b in tec if b["text"].startswith("“")), None)
testo_tec = "\n".join(
    f"<p>{e(b['text'])}</p>" for b in tec if b["type"] == "paragraph" and b["text"] != cita
)
fig_tec = next((b for b in cat["tecnica"] if b["type"] == "figure"), None)
d_tec = dim(fig_tec["src"]) if fig_tec else None

corpo_tecnica = f"""
<section class="intestazione-pagina">
  <div class="contenitore stretto">
    <p class="occhiello">Il metodo</p>
    <h1>La tecnica</h1>
    <p class="guida">Una tecnica basata sull’istinto.</p>
  </div>
</section>
<section class="sezione" style="padding-top:0">
  <div class="contenitore stretto testo-lungo">
    {f'<h2 style="color:var(--accento)">{e(cita)}</h2>' if cita else ''}
    {testo_tec}
    {f'''<figure><img src="img/full/{web(fig_tec["src"])}" width="{d_tec['w']}" height="{d_tec['h']}"
       loading="lazy" decoding="async" alt="Opera di Maurizio Bertino"
       data-grande="img/full/{web(fig_tec["src"])}" data-titolo="" data-dati=""></figure>''' if fig_tec else ''}
  </div>
</section>
"""
pagina("tecnica.html", "La tecnica — Maurizio Bertino",
       "«Un’arte espressionista e non accademica». Come nascono le opere di Maurizio Bertino: "
       "pennello, scalpello e le mani nella terracotta.",
       corpo_tecnica, og=fig_tec["src"] if fig_tec else EROE)


# ---------------------------------------------------------------- NATIVI
def togli_prefisso(testo, titolo):
    """Toglie il titolo dall'inizio della didascalia ignorando la punteggiatura.
    Serve perche' i titoli sono stati ripuliti ("Mato-Tope.(capo" -> "Mato-Tope (capo")
    mentre le didascalie conservano la forma originale."""
    def norm(x):
        return re.sub(r"[^0-9a-z\u00e0-\u00ff]", "", x.lower())
    atteso = norm(titolo)
    if not atteso:
        return testo
    acc = ""
    for i, ch in enumerate(testo):
        acc = norm(acc + ch)
        if acc == atteso:
            return testo[i + 1:].lstrip(" ,.;:)]}\u2019\u201d\"'").strip()
        if not atteso.startswith(acc):
            return testo
    return ""


def collega_articolo(titolo):
    """Trova l'articolo che approfondisce una riproduzione, se esiste."""
    stop = {"di", "a", "con", "in", "e", "il", "la", "le", "una", "un", "da",
            "della", "delle", "dei", "del", "nello", "stile", "riproduzione",
            "personale", "club", "war", "headed", "variante", "cm", "circa"}
    def token(t):
        return {p for p in re.findall(r"[a-zà-ù]+", t.lower()) if p not in stop and len(p) > 2}
    a_t = token(titolo)
    if not a_t:
        return None
    migliore, punteggio = None, 0
    for art in cat["articoli"]:
        s = len(a_t & token(art["titolo"]))
        if s > punteggio:
            migliore, punteggio = art, s
    return migliore if punteggio >= 2 else None


schede = ""
collegati = []
for n in cat["nativi"]:
    d = dim(n["img"])
    art = collega_articolo(n["titolo"])
    if art:
        collegati.append((n["titolo"], art["titolo"]))
    dettaglio = togli_prefisso(n["didascalia"], n["titolo"])
    schede += f"""
      <article class="scheda appare">
        <span class="scatto" data-grande="img/full/{web(n['img'])}"
              data-titolo="{e(n['titolo'])}" data-dati="{e(dettaglio)}">
          <img src="img/thumb/{web(n['img'])}" width="{d['w']}" height="{d['h']}"
            loading="lazy" decoding="async" alt="{e(n['titolo'])}">
        </span>
        <div class="testo">
          <h3>{e(n['titolo'])}</h3>
          {f"<p>{e(dettaglio)}</p>" if dettaglio else ""}
          {f'<a class="approfondisci" href="articoli/{art["slug"]}.html">Leggi la scheda &rarr;</a>' if art else ''}
        </div>
      </article>"""

intro_nativi = "\n".join(f"<p>{e(b['text'])}</p>" for b in cat["intro_nativi"][:3])
corpo_nativi = f"""
<section class="intestazione-pagina">
  <div class="contenitore stretto">
    <p class="occhiello">La passione</p>
    <h1>I nativi d’America</h1>
  </div>
</section>
<section class="sezione" style="padding-top:0">
  <div class="contenitore stretto testo-lungo">
    {intro_nativi}
  </div>
</section>
<section class="sezione alt">
  <div class="contenitore">
    <p class="occhiello">Le riproduzioni</p>
    <h2>Manufatti riprodotti e personalizzati</h2>
    <p class="guida">Riproduzioni di manufatti di vario genere, con aggiunta di
       personalizzazione: archi, frecce, faretre e vestigia, vestiario vario,
       nonché collane, piccole borse decorate con perline, tracolla indiana
       personalizzata in pelle. Tocca una foto per ingrandirla.</p>
    <div class="schede" style="margin-top:36px">{schede}
    </div>
  </div>
</section>
"""
pagina("nativi.html", "La passione per i nativi d’America — Maurizio Bertino",
       "Archi, faretre, collane e vestiario: i manufatti dei popoli nativi "
       "nordamericani riprodotti e personalizzati da Maurizio Bertino.",
       corpo_nativi, og=cat["nativi"][0]["img"] if cat["nativi"] else EROE)


# ---------------------------------------------------------------- DIARIO
righe = ""
for a in cat["articoli"]:
    d = dim(a["cover"]) if a["cover"] else {"w": 800, "h": 600}
    righe += f"""
      <article class="articolo-riga">
        <a class="scatto" href="articoli/{a['slug']}.html" aria-hidden="true" tabindex="-1">
          <img src="img/thumb/{web(a['cover'])}" width="{d['w']}" height="{d['h']}"
            loading="lazy" decoding="async" alt="">
        </a>
        <div>
          <p class="data">{e(a['data_it'])}</p>
          <h3><a href="articoli/{a['slug']}.html">{e(a['titolo'])}</a></h3>
          <p>{e(estratto(a))}</p>
        </div>
      </article>"""

corpo_diario = f"""
<section class="intestazione-pagina">
  <div class="contenitore stretto">
    <p class="occhiello">Diario</p>
    <h1>Schede e appunti</h1>
    <p class="guida">Le schede di approfondimento sulle singole opere: materiali,
       epoca, cultura di riferimento e come sono state realizzate.</p>
  </div>
</section>
<section class="sezione" style="padding-top:0">
  <div class="contenitore stretto">
    <div class="elenco-articoli">{righe}
    </div>
  </div>
</section>
"""
pagina("diario.html", "Diario — Maurizio Bertino",
       "Schede di approfondimento sulle opere di Maurizio Bertino: materiali, "
       "epoca e tecniche di realizzazione.",
       corpo_diario, og=cat["articoli"][0]["cover"] if cat["articoli"] else EROE)


# ---------------------------------------------------------------- ARTICOLI
for i, a in enumerate(cat["articoli"]):
    prec = cat["articoli"][i + 1] if i + 1 < len(cat["articoli"]) else None
    succ = cat["articoli"][i - 1] if i > 0 else None
    nav_art = []
    if succ:
        nav_art.append(f'<a href="{succ["slug"]}.html">&larr; {e(succ["titolo"])}</a>')
    if prec:
        nav_art.append(f'<a href="{prec["slug"]}.html">{e(prec["titolo"])} &rarr;</a>')

    corpo = f"""
<section class="intestazione-pagina">
  <div class="contenitore stretto">
    <p class="occhiello"><a href="../diario.html" style="text-decoration:none">Diario</a> · {e(a['data_it'])}</p>
    <h1>{e(a['titolo'])}</h1>
  </div>
</section>
<section class="sezione" style="padding-top:0">
  <div class="contenitore stretto testo-lungo">
    {blocchi_html(a['blocchi'], su='../')}
  </div>
</section>
<section class="sezione alt">
  <div class="contenitore stretto">
    <p class="occhiello">Continua</p>
    <div class="piede" style="border:0;background:none;padding:0;margin:0">
      <div style="display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between;width:100%">
        {''.join(nav_art) if nav_art else '<a href="../diario.html">Torna al diario</a>'}
      </div>
    </div>
  </div>
</section>
"""
    pagina(f"articoli/{a['slug']}.html", f"{a['titolo']} — Maurizio Bertino",
           estratto(a, 155) or a["titolo"], corpo, su="../", og=a["cover"])


# ---------------------------------------------------------------- CONTATTI
wa = re.sub(r"\D", "", CONTATTI["whatsapp"])
SVG = {
    "mail": '<path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/>',
    "wa": '<path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 21l2.2-5.2A8.5 8.5 0 1 1 21 11.5Z"/>'
          '<path d="M8.6 9.2c.3 2.7 3.5 5.9 6.2 6.2l1.2-1.4-1.9-1-1 .9c-1-.5-2.1-1.6-2.6-2.6l.9-1-1-1.9-1.8 1.2Z"/>',
    "fb": '<path d="M14 8h3V5h-3a4 4 0 0 0-4 4v2H8v3h2v7h3v-7h3l1-3h-4V9a1 1 0 0 1 1-1Z"/>',
    "yt": '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/>'
          '<path d="m10.5 9.5 5 2.5-5 2.5Z"/>',
}


def contatto(icona, etichetta, valore, href, grezzo=False):
    testo = valore if grezzo else e(valore)
    return f"""
    <a class="contatto" href="{href}"{' target="_blank" rel="noopener"' if href.startswith('http') else ''}>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"
           stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVG[icona]}</svg>
      <span>
        <span class="etichetta">{etichetta}</span><br>
        <span class="valore">{testo}</span>
      </span>
    </a>"""


# l'indirizzo email va spezzato alla chiocciola, non a metà parola
email_visibile = e(CONTATTI["email"]).replace("@", "<wbr>@")


corpo_contatti = f"""
<section class="intestazione-pagina">
  <div class="contenitore stretto">
    <p class="occhiello">Contatti</p>
    <h1>Scrivimi</h1>
    <p class="guida">Sei interessato a un’opera o vuoi saperne di più sulla mia arte?
       Scegli il canale che preferisci: rispondo personalmente.</p>
  </div>
</section>
<section class="sezione" style="padding-top:0">
  <div class="contenitore stretto">
    <div class="contatti">
      {contatto('mail', 'Email', email_visibile, 'mailto:' + CONTATTI['email'], grezzo=True)}
      {contatto('wa', 'WhatsApp', '331 438 5178', f'https://wa.me/{wa}')}
      {contatto('fb', 'Facebook', 'Seguimi su Facebook', CONTATTI['facebook'])}
      {contatto('yt', 'YouTube', 'Guarda i video', CONTATTI['youtube'])}
    </div>
  </div>
</section>
"""
pagina("contatti.html", "Contatti — Maurizio Bertino",
       "Contatta Maurizio Bertino per informazioni sulle opere: email, WhatsApp e social.",
       corpo_contatti)


# ---------------------------------------------------------------- 404
pagina("404.html", "Pagina non trovata — Maurizio Bertino",
       "La pagina cercata non esiste.", """
<section class="sezione" style="min-height:52vh;display:flex;align-items:center">
  <div class="contenitore stretto" style="text-align:center">
    <p class="occhiello">Errore 404</p>
    <h1>Questa pagina non esiste</h1>
    <p class="guida" style="margin:0 auto 28px">Forse è stata spostata, o l’indirizzo è sbagliato.</p>
    <p><a href="index.html">Torna alla home</a> &nbsp;·&nbsp; <a href="opere.html">Vai alle opere</a></p>
  </div>
</section>
""")


# ---------------------------------------------------------------- extra
open(os.path.join(SITO, "robots.txt"), "w").write(
    f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n")

url_tutti = [f[0] for f in PAGINE] + [f"articoli/{a['slug']}.html" for a in cat["articoli"]]
voci = "\n".join(
    f"  <url><loc>{DOMINIO}/{'' if u == 'index.html' else u}</loc>"
    f"<changefreq>monthly</changefreq><priority>{'1.0' if u == 'index.html' else '0.7'}</priority></url>"
    for u in url_tutti)
open(os.path.join(SITO, "sitemap.xml"), "w", encoding="utf-8").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n'
    f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{voci}\n</urlset>\n')

print(f"Pagine generate: {len(url_tutti) + 1} (incluso 404)")
print(f"Opere in catalogo: {len(op)}  |  schede native: {len(cat['nativi'])}  |  articoli: {len(cat['articoli'])}")
print("\nSchede native collegate al relativo articolo:")
for a, b in collegati:
    print(f"  · {a[:52]:<54} -> {b}")
print(f"  ({len(collegati)} di {len(cat['nativi'])})")
