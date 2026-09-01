#!/usr/bin/env python3
# Genera le immagini delle uscite social nei tre formati, a partire dalle foto
# gia' presenti in sito/img/full. Non ritaglia mai l'opera: la contiene su fondo
# carta, come una stampa su cartoncino. Si rilancia quando serve: e' idempotente.
#
#   python3 social/genera-social.py
#
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(BASE, "sito", "img", "full")
OUT  = os.path.join(BASE, "social", "uscite")

CARTA     = (250, 247, 242)
INCHIOSTRO= (28, 25, 23)
TENUE     = (107, 98, 90)
BORDO     = (226, 218, 205)

F = "/System/Library/Fonts/Supplemental/"
def font(nome, dim):
    return ImageFont.truetype(F + nome, dim)

FORMATI = {
    # nome        larghezza altezza  margine_x  box_altezza  testo
    "quadrato":  (1080, 1080,  90,  900, False),
    "verticale": (1080, 1350,  90, 1130, False),
    "storia":    (1080, 1920, 100, 1150, True),
}

def componi(sorgente, dest, formato, titolo, meta):
    W, H, mx, box_h, con_testo = FORMATI[formato]
    tela = Image.new("RGB", (W, H), CARTA)
    op = Image.open(sorgente).convert("RGB")

    box_w = W - 2 * mx
    scala = min(box_w / op.width, box_h / op.height)
    nw, nh = int(op.width * scala), int(op.height * scala)
    op = op.resize((nw, nh), Image.LANCZOS)

    if con_testo:
        # opera in alto, testo sotto: la storia ha spazio da riempire
        y = 260 + (box_h - nh) // 2
    else:
        y = (H - nh) // 2
    x = (W - nw) // 2
    tela.paste(op, (x, y))

    d = ImageDraw.Draw(tela)
    d.rectangle([x - 1, y - 1, x + nw, y + nh], outline=BORDO, width=2)

    if con_testo:
        ty = y + nh + 90
        f_tit = font("Georgia.ttf", 58)
        f_met = font("Georgia Italic.ttf", 36)
        f_fir = font("Georgia.ttf", 30)
        for riga in avvolgi(d, titolo, f_tit, W - 2 * mx):
            d.text((W // 2, ty), riga, font=f_tit, fill=INCHIOSTRO, anchor="ma")
            ty += 74
        if meta:
            ty += 14
            d.text((W // 2, ty), meta, font=f_met, fill=TENUE, anchor="ma")
        d.line([(W // 2 - 60, H - 190), (W // 2 + 60, H - 190)], fill=BORDO, width=2)
        d.text((W // 2, H - 150), "Maurizio Bertino", font=f_fir, fill=TENUE, anchor="ma")

    tela.save(dest, "JPEG", quality=90, optimize=True, progressive=True)
    return os.path.getsize(dest)

def avvolgi(d, testo, f, larghezza):
    parole, righe, riga = testo.split(), [], ""
    for p in parole:
        prova = (riga + " " + p).strip()
        if d.textlength(prova, font=f) <= larghezza:
            riga = prova
        else:
            if riga: righe.append(riga)
            riga = p
    if riga: righe.append(riga)
    return righe

def main():
    piano = json.load(open(os.path.join(BASE, "social", "uscite.json")))
    for u in piano:
        cartella = os.path.join(OUT, u["cartella"])
        os.makedirs(cartella, exist_ok=True)
        src = os.path.join(FULL, u["img"])
        if not os.path.exists(src):
            print("MANCA:", src); sys.exit(1)
        for fmt in FORMATI:
            dest = os.path.join(cartella, f"{fmt}.jpg")
            kb = componi(src, dest, fmt, u["titolo_img"], u["meta_img"]) // 1024
            print(f"  {u['cartella']}/{fmt}.jpg  {kb} KB")

if __name__ == "__main__":
    main()
