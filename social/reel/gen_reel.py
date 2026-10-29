# -*- coding: utf-8 -*-
"""Reel «tipo Superquark» di un dipinto (28/10/2026): voce da documentario, la camera va da un
particolare all'altro di una foto ferma.

Davide, 28/10: «avevo pensato a dei reel tipo Superquark, con la voce da documentario, dove magari
facevamo vedere dettagli dell'opera». Il primo, di prova, è su «Tempi remoti» (tempi-remoti/).

Come è fatto:
- fondo scuro; il quadro sta in una finestra 1080×960 fra il 14 % in alto e il 35 % in basso dello
  schermo, cioè fuori da icone, didascalia e pulsanti dei Reels (guida Meta, come i reel di SE2);
- una frase della voce per inquadratura: ogni frase è un mp3 a sé (ElevenLabs, eleven.py), così i
  tempi delle inquadrature e dei sottotitoli vengono dalle durate, senza whisper;
- le foto arrivano a 1600 px: la finestra non si stringe sotto i 600 px di quadro (circa 1,8×),
  oltre il dettaglio si sfoca (prova del 28/10);
- caratteri del sito: Iowan Old Style; colore d'accento del sito, #e2915f;
- in chiusura dissolvenza sul fondo chiaro del sito (--carta, #faf7f2) col logo di Maurizio
  (pennellata rossa e nome in grigio scuro, che sul fondo scuro non si leggerebbe). Davide, 28/10:
  «alla fine: transizione e farei vedere il logo di Maurizio».

Uso:  /usr/bin/python3 gen_reel.py tempi-remoti      (Pillow sta nel Python di sistema)
      /usr/bin/python3 gen_reel.py tempi-remoti --prove   (solo i fotogrammi chiave, niente voce)
"""
import importlib.util, json, math, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)

W, H = 1080, 1920
FIN_Y, FIN_W, FIN_H = 270, 1080, 960          # finestra del quadro (aspetto 9:8)
FPS = 30
PAUSA = 0.45                                   # silenzio fra una frase e l'altra
MOSSA = 0.9                                    # secondi del movimento fra due inquadrature
FONDO = (20, 18, 16)
ACCENTO = (226, 145, 95)
SERIF = "/System/Library/Fonts/Supplemental/Iowan Old Style.ttc"
CARTA = (250, 247, 242)
LOGO = os.path.join(QUI, "..", "..", "immagini", "cropped-logo-bertizio-1.png")
FINALE, DISSOLVENZA = 3.2, 1.0                 # secondi del logo in chiusura, e della dissolvenza


def carica(cartella):
    spec = importlib.util.spec_from_file_location("opera", os.path.join(QUI, cartella, "opera.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def tela(foto, margine=500):
    """Il quadro su un fondo scuro largo, così un'inquadratura può uscire dal bordo del dipinto."""
    im = Image.open(foto).convert("RGB")
    c = Image.new("RGB", (im.width + 2 * margine, im.height + 2 * margine), FONDO)
    c.paste(im, (margine, margine))
    return c, margine, im.size


def ritaglio(c, m, rett):
    cx, cy, w = rett
    h = w * FIN_H / FIN_W
    box = (cx - w / 2 + m, cy - h / 2 + m, cx + w / 2 + m, cy + h / 2 + m)
    return c.resize((FIN_W, FIN_H), Image.LANCZOS, box=box)


def morbido(t):
    return 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, t)))


def misto(a, b, t):
    # lo zoom si interpola sul logaritmo della larghezza: il movimento sembra costante
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t,
            math.exp(math.log(a[2]) + (math.log(b[2]) - math.log(a[2])) * t))


def a_capo(testo, font, larg, d):
    righe, riga = [], ""
    for p in testo.split():
        prova = (riga + " " + p).strip()
        if d.textlength(prova, font=font) <= larg:
            riga = prova
        else:
            righe.append(riga); riga = p
    return righe + [riga]


def fotogramma(base, finestra, sott, alfa_fin=1.0, chiusura=None):
    f = base.copy()
    if alfa_fin < 1:
        finestra = Image.blend(Image.new("RGB", finestra.size, FONDO), finestra, alfa_fin)
    f.paste(finestra, (0, FIN_Y))
    d = ImageDraw.Draw(f)
    if sott:
        font = ImageFont.truetype(SERIF, 50)
        righe = a_capo(sott, font, W - 2 * 90, d)
        y = FIN_Y + FIN_H + 70
        for r in righe:
            d.text((W / 2, y), r, font=font, fill=(240, 234, 226), anchor="ma")
            y += 66
    if chiusura:
        # cartello finale: titolo, autore e anno, sito (dissolvenza da 0 a 1)
        a = chiusura
        col = lambda c: tuple(int(FONDO[i] + (c[i] - FONDO[i]) * a) for i in range(3))
        titolo, sotto = chiusura_testo
        d.text((W / 2, FIN_Y + FIN_H + 70), titolo, font=ImageFont.truetype(SERIF, 66),
               fill=col((240, 234, 226)), anchor="ma")
        d.text((W / 2, FIN_Y + FIN_H + 162), sotto, font=ImageFont.truetype(SERIF, 40),
               fill=col((200, 192, 182)), anchor="ma")
        d.text((W / 2, FIN_Y + FIN_H + 236), "artemauriziobertino.com", font=ImageFont.truetype(SERIF, 44),
               fill=col(ACCENTO), anchor="ma")
    return f


chiusura_testo = ("", "")


def durata(file):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                 "csv=p=0", file], capture_output=True, text=True, check=True).stdout)


def main():
    global chiusura_testo
    cartella = sys.argv[1]
    op = carica(cartella)
    dove = os.path.join(QUI, cartella)
    c, m, (iw, ih) = tela(op.FOTO)
    chiusura_testo = op.CHIUSURA
    base = Image.new("RGB", (W, H), FONDO)

    if "--prove" in sys.argv:
        for i, s in enumerate(op.SCENE, 1):
            for k, r in (("a", s["da"]), ("b", s["a"])):
                fotogramma(base, ritaglio(c, m, r), s.get("sott", s["voce"])).save(os.path.join(dove, f"prova-{i:02d}{k}.jpg"), quality=80)
        print("fotogrammi di prova in", dove); return

    import eleven
    tmp = tempfile.mkdtemp()
    # 1. voce, una frase per scena
    tempi, t = [], 0.6
    for i, s in enumerate(op.SCENE, 1):
        mp3 = os.path.join(tmp, f"v{i:02d}.mp3")
        eleven.leggi(s["voce"], mp3, op.VOCE, impostazioni=op.IMPOSTAZIONI)
        d = durata(mp3)
        tempi.append((t, t + d, mp3)); t += d + PAUSA
    t_logo = t + op.CODA
    fine = t_logo + FINALE
    logo = Image.open(LOGO).convert("RGBA").resize((900, 900), Image.LANCZOS)
    cartello_logo = Image.new("RGB", (W, H), CARTA)
    cartello_logo.paste(logo, ((W - 900) // 2, (H - 900) // 2 - 60), logo)

    # 2. immagini
    proc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                             "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                             "-crf", "23", "-pix_fmt", "yuv420p", os.path.join(tmp, "video.mp4")],
                            stdin=subprocess.PIPE)
    n = int(fine * FPS)
    for k in range(n):
        tt = k / FPS
        # scena corrente: quella cominciata per ultima (la camera parte MOSSA/2 prima della voce)
        i = max([j for j, (a, _, _) in enumerate(tempi) if tt >= a - MOSSA / 2] or [0])
        s = op.SCENE[i]
        a, b, _ = tempi[i]
        fine_scena = tempi[i + 1][0] - MOSSA / 2 if i + 1 < len(tempi) else fine
        inizio = a - MOSSA / 2
        prec = op.SCENE[i - 1]["a"] if i > 0 else s["da"]
        if tt < inizio + MOSSA and i > 0:
            r = misto(prec, s["da"], morbido((tt - inizio) / MOSSA))
        else:
            r = misto(s["da"], s["a"], morbido((tt - inizio - MOSSA) / max(0.1, fine_scena - inizio - MOSSA)))
        sott = s.get("sott", s["voce"]) if a - 0.1 <= tt <= b + 0.2 else ""
        chiusura = None
        da = op.CHIUSURA_DA - 1                         # dalla scena del titolo: cartello al posto dei sottotitoli
        if i >= da:
            sott = ""
            chiusura = min(1, max(0, (tt - tempi[da][0] + 0.3) / 0.8))
        alfa = min(1, tt / 0.6)                       # apertura dal nero
        f = fotogramma(base, ritaglio(c, m, r), sott, alfa_fin=1, chiusura=chiusura)
        if alfa < 1:
            f = Image.blend(Image.new("RGB", f.size, (0, 0, 0)), f, alfa)
        if tt >= t_logo:                              # chiusura sul logo
            f = Image.blend(f, cartello_logo, morbido((tt - t_logo) / DISSOLVENZA))
        proc.stdin.write(f.tobytes())
    proc.stdin.close(); proc.wait()

    # 3. audio: voce alle sue posizioni, musica sotto, effetti
    entrate, filtri = ["-i", os.path.join(tmp, "video.mp4")], []
    for j, (a, _, mp3) in enumerate(tempi, 1):
        entrate += ["-i", mp3]
        filtri.append(f"[{j}:a]adelay={int(a*1000)}|{int(a*1000)},volume=1.0[v{j}]")
    mix = "".join(f"[v{j}]" for j in range(1, len(tempi) + 1))
    nmix = len(tempi)
    extra = 0
    if getattr(op, "MUSICA", None):
        entrate += ["-stream_loop", "-1", "-i", op.MUSICA]
        q = len(tempi) + 1
        filtri.append(f"[{q}:a]volume={op.VOL_MUSICA},afade=t=in:d=1.5,afade=t=out:st={fine-2.5:.2f}:d=2.5,atrim=0:{fine:.2f}[mu]")
        mix += "[mu]"; nmix += 1; extra = 1
    # suoni d'ambiente (in loop per tutto il reel, sotto la voce) ed effetti puntuali
    for a_i, (file, vol) in enumerate(getattr(op, "AMBIENTE", [])):
        entrate += ["-stream_loop", "-1", "-i", file]
        q = len(tempi) + 1 + extra
        filtri.append(f"[{q}:a]volume={vol},afade=t=in:d=2,afade=t=out:st={fine-2.5:.2f}:d=2.5,atrim=0:{fine:.2f}[a{a_i}]")
        mix += f"[a{a_i}]"; nmix += 1; extra += 1
    for e_i, (file, vol, quando) in enumerate(getattr(op, "EFFETTI", [])):
        # quando: secondi dall'inizio, oppure (scena, scarto) = secondi dall'inizio della frase di quella scena
        istante = quando if isinstance(quando, (int, float)) else tempi[quando[0] - 1][0] + quando[1]
        entrate += ["-i", file]
        q = len(tempi) + 1 + extra + e_i
        filtri.append(f"[{q}:a]volume={vol},adelay={int(istante*1000)}|{int(istante*1000)}[e{e_i}]")
        mix += f"[e{e_i}]"; nmix += 1
    filtri.append(f"{mix}amix=inputs={nmix}:normalize=0:duration=longest,alimiter=limit=0.89:level=false,atrim=0:{fine:.2f}[aout]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entrate, "-filter_complex", ";".join(filtri),
                    "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", op.USCITA], check=True)
    json.dump([(round(a, 2), round(b, 2)) for a, b, _ in tempi], open(os.path.join(dove, "tempi.json"), "w"))
    print(op.USCITA, f"{fine:.1f} s")


if __name__ == "__main__":
    main()
