#!/usr/bin/env python3
"""Aggiunge un articolo al Diario: lo inserisce in _catalogo.json (campo
`articoli`, il più recente in testa) e rigenera il sito.

Uso:
  python3 aggiungi-articolo.py TESTO.txt --titolo "Titolo" --cover img_4510.jpg \
      [--data 2026-11-16] [--slug un-titolo] [--opera "Titolo dell'opera"]

TESTO.txt: i paragrafi separati da una riga vuota. Una riga che comincia con
"## " è un titoletto; una riga "[foto: nome.jpg]" è una foto già in sito/img/full
(le dimensioni devono stare in _dimensioni.json: le foto passano da aggiungi-opera.py).
`--opera` è il titolo esatto dell'opera nel catalogo: collega l'articolo alla sua
scheda («Leggi l'articolo» nel visore di Opere e nei Nativi).
Si ferma, senza cambiare niente, se lo slug o il titolo esistono già, se la copertina
o una foto non ci sono, o se `--opera` non è un titolo del catalogo.
"""
import argparse, datetime, json, os, re, subprocess, sys, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.normpath(os.path.join(BASE, ".."))
FULL = os.path.join(PROG, "sito", "img", "full")
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]

p = argparse.ArgumentParser()
p.add_argument("testo", help="file di testo con l'articolo")
p.add_argument("--titolo", required=True)
p.add_argument("--cover", required=True, help="foto di copertina, già in sito/img/full")
p.add_argument("--data", default=datetime.date.today().isoformat(), help="AAAA-MM-GG")
p.add_argument("--slug", default=None)
p.add_argument("--opera", default=None, help="titolo dell'opera nel catalogo")
a = p.parse_args()


def norm(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


slug = a.slug or re.sub(r"\s+", "-", norm(a.titolo))
fcat = os.path.join(BASE, "_catalogo.json")
cat = json.load(open(fcat, encoding="utf-8"))
dims = json.load(open(os.path.join(BASE, "_dimensioni.json"), encoding="utf-8"))

for art in cat["articoli"]:
    if art["slug"] == slug or norm(art["titolo"]) == norm(a.titolo):
        sys.exit(f"Esiste già un articolo '{art['titolo']}' ({art['slug']}). Nessuna modifica.")
    if a.opera and art.get("opera") and norm(art["opera"]) == norm(a.opera):
        sys.exit(f"L'opera '{a.opera}' ha già l'articolo '{art['titolo']}'. Nessuna modifica.")
if a.opera and not any(norm(o["titolo"]) == norm(a.opera) for o in cat["opere"]):
    sys.exit(f"'{a.opera}' non è un titolo del catalogo (opere). Nessuna modifica.")
try:
    d = datetime.date.fromisoformat(a.data)
except ValueError:
    sys.exit("La data va scritta AAAA-MM-GG.")


def controlla_foto(nome):
    if not os.path.isfile(os.path.join(FULL, nome)):
        sys.exit(f"Foto non trovata in sito/img/full: {nome}")
    if nome not in dims:
        sys.exit(f"Dimensioni mancanti in _dimensioni.json per {nome}")


controlla_foto(a.cover)
blocchi = []
for pezzo in re.split(r"\n\s*\n", open(a.testo, encoding="utf-8").read().strip()):
    pezzo = pezzo.strip()
    m = re.fullmatch(r"\[foto:\s*(.+?)\s*\]", pezzo)
    if m:
        controlla_foto(m.group(1))
        im = dims[m.group(1)]
        blocchi.append({"type": "figure", "src": m.group(1), "caption": None,
                        "w": str(im["w"]), "h": str(im["h"])})
    elif pezzo.startswith("## "):
        blocchi.append({"type": "heading", "level": "h3", "text": pezzo[3:].strip()})
    else:
        blocchi.append({"type": "paragraph", "level": "p",
                        "text": re.sub(r"\s*\n\s*", " ", pezzo)})

art = {"slug": slug, "titolo": a.titolo, "data": a.data,
       "data_it": f"{d.day} {MESI[d.month - 1]} {d.year}", "cover": a.cover,
       "blocchi": blocchi}
if a.opera:
    art["opera"] = a.opera
# il più recente in testa (le pagine «precedente/successivo» seguono quest'ordine)
pos = next((i for i, x in enumerate(cat["articoli"]) if x["data"] <= a.data), len(cat["articoli"]))
cat["articoli"].insert(pos, art)
json.dump(cat, open(fcat, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

subprocess.run([sys.executable, os.path.join(BASE, "genera.py")], check=True, capture_output=True)
print(f"Aggiunto: {a.titolo}  ->  sito/articoli/{slug}.html  (posizione {pos + 1} di {len(cat['articoli'])})")
if a.opera:
    print(f"  collegato all'opera: {a.opera}")
