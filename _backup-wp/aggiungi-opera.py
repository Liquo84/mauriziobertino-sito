#!/usr/bin/env python3
"""Aggiunge un'opera al catalogo: copia la foto, crea le versioni web,
inserisce la scheda e rigenera il sito.

Uso:
  python3 aggiungi-opera.py FOTO --sezione pittura --titolo "Nome opera" \
      [--misure "80x60"] [--anno 2024] [--tecnica "Olio su tela"]
"""
import argparse, json, os, shutil, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.normpath(os.path.join(BASE, ".."))
ORIG = os.path.join(PROG, "immagini")
FULL = os.path.join(PROG, "sito", "img", "full")
THUMB = os.path.join(PROG, "sito", "img", "thumb")

p = argparse.ArgumentParser()
p.add_argument("foto", help="percorso della foto originale")
p.add_argument("--sezione", required=True, choices=["pittura", "scultura", "nativi"])
p.add_argument("--titolo", required=True)
p.add_argument("--misure", default=None, help='es. "80x60" oppure "36 cm"')
p.add_argument("--anno", default=None)
p.add_argument("--tecnica", default=None)
p.add_argument("--nome-file", default=None, help="rinomina il file (senza estensione)")
p.add_argument("--viste", nargs="*", default=[],
               help="altre foto della stessa opera (altri lati, dettagli)")
a = p.parse_args()

if not os.path.isfile(a.foto):
    sys.exit(f"Foto non trovata: {a.foto}")


def sips(sorgente, destinazione, lato, qualita):
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", str(qualita),
                    "-Z", str(lato), sorgente, "--out", destinazione],
                   check=True, capture_output=True)


def dimensioni(percorso):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", percorso],
                         check=True, capture_output=True, text=True).stdout
    d = {}
    for riga in out.splitlines():
        if "pixelWidth" in riga:
            d["w"] = int(riga.split(":")[1])
        elif "pixelHeight" in riga:
            d["h"] = int(riga.split(":")[1])
    return d


# --- 1. copia l'originale nell'archivio -----------------------------------
radice = a.nome_file or os.path.splitext(os.path.basename(a.foto))[0]
radice = radice.strip().replace(" ", "-").lower()
ext = os.path.splitext(a.foto)[1] or ".jpg"
originale = os.path.join(ORIG, radice + ext)
if os.path.abspath(a.foto) != os.path.abspath(originale):
    shutil.copy2(a.foto, originale)

# --- 2. versioni per il web ------------------------------------------------
sips(originale, os.path.join(FULL, radice + ".jpg"), 1800, 80)
sips(originale, os.path.join(THUMB, radice + ".jpg"), 640, 60)

# --- 3. dimensioni ---------------------------------------------------------
fdim = os.path.join(BASE, "_dimensioni.json")
dim = json.load(open(fdim, encoding="utf-8"))
dim[radice + ".jpg"] = dimensioni(os.path.join(THUMB, radice + ".jpg"))
json.dump(dim, open(fdim, "w", encoding="utf-8"))

# --- 3bis. altre viste della stessa opera ---------------------------------
viste = []
for k, extra in enumerate(a.viste, start=2):
    if not os.path.isfile(extra):
        sys.exit(f"Vista non trovata: {extra}")
    nome = f"{radice}-vista{k}"
    orig_v = os.path.join(ORIG, nome + os.path.splitext(extra)[1])
    if os.path.abspath(extra) != os.path.abspath(orig_v):
        shutil.copy2(extra, orig_v)
    sips(orig_v, os.path.join(FULL, nome + ".jpg"), 1800, 80)
    viste.append(nome + ".jpg")

# --- 4. scheda nel catalogo ------------------------------------------------
fcat = os.path.join(BASE, "_catalogo.json")
cat = json.load(open(fcat, encoding="utf-8"))

misure = a.misure
if misure:
    misure = misure.replace("x", "×").replace(" ", "")
    if not misure.endswith("cm"):
        misure += " cm"
    misure = misure.replace("cm", " cm").replace("  ", " ").strip()

pezzi = [x for x in (misure, a.anno, a.tecnica) if x]
scheda = {
    "n": None,
    "titolo": a.titolo,
    "misure": misure,
    "anno": a.anno,
    "tecnica": a.tecnica,
    "didascalia": ", ".join([a.titolo] + pezzi),
    "img": radice + ext,
    "w": None, "h": None,
    "sezione": a.sezione,
}
if viste:
    scheda["viste"] = viste

if any(o["img"] == scheda["img"] for o in cat["opere"]):
    sys.exit(f"Attenzione: '{radice}' è già in catalogo. Nessuna modifica.")

# inserisce in fondo alle opere della stessa sezione
ultimo = max((i for i, o in enumerate(cat["opere"]) if o["sezione"] == a.sezione),
             default=len(cat["opere"]) - 1)
cat["opere"].insert(ultimo + 1, scheda)
json.dump(cat, open(fcat, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# --- 5. rigenera -----------------------------------------------------------
subprocess.run([sys.executable, os.path.join(BASE, "genera.py")], check=True,
               capture_output=True)

from collections import Counter
print(f"Aggiunta: {a.titolo}  [{a.sezione}]")
print(f"  originale -> immagini/{radice}{ext}")
print(f"  web       -> sito/img/full/{radice}.jpg  +  sito/img/thumb/{radice}.jpg")
print(f"  didascalia: {scheda['didascalia']}")
if viste:
    print(f"  viste aggiuntive: {len(viste)} ({', '.join(viste)})")
print(f"  catalogo ora: {dict(Counter(o['sezione'] for o in cat['opere']))}")
