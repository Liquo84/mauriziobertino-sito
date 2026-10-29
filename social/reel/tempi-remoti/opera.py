# -*- coding: utf-8 -*-
"""Reel di prova «Tempi remoti» (28/10/2026). Testo della voce: riscritto e rivisto dal copywriter il 29/10
sul commento scritto di Maurizio (VOCE.md, banca fatti), con le emozioni e gli effetti chiesti da Davide:
«oltre che descrivere mi piacerebbe molto raccontare anche le emozioni, anche mettere qualche effetto
audio per aiutare l'immersione». Dati dell'opera: Maurizio, chat del 24/10.
Inquadrature: (centro x, centro y, larghezza) in pixel della foto 1600×1293; mai sotto 600 di larghezza.
"""
import os
QUI = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.abspath(os.path.join(QUI, "..", "..", ".."))
FOTO = os.path.join(PROG, "immagini", "tempi-remoti.JPG")
USCITA = os.path.join(QUI, "2026-10-29 Reel prova - Tempi remoti.mp4")

VOCE = "HuK8QKF35exsCh2e7fLT"          # Carmelo La Rosa, voce italiana già nell'account (libreria ElevenLabs)
IMPOSTAZIONI = {"stability": 0.6, "similarity_boost": 0.75, "speed": 0.92}
CODA = 2.5                             # secondi di cartello finale dopo l'ultima frase
CHIUSURA = ("Tempi remoti", "Maurizio Bertino, 1997")
CHIUSURA_DA = 10                       # dalla frase del titolo il cartello prende il posto dei sottotitoli

INTERO = (800, 646, 1600)
SCENE = [
    {"voce": "È Natale, dentro un casolare. Una famiglia fa festa con quel poco che ha.", "da": INTERO, "a": (800, 646, 1450)},
    {"voce": "Il camino acceso, la fiamma alta. Sopra, una treccia d'aglio.",
     "da": (330, 760, 660), "a": (320, 360, 620)},
    {"voce": "Marito e moglie, di mezza età. Lei, col fazzoletto azzurro, gli posa le mani sulle spalle.",
     "da": (1060, 250, 640), "a": (1090, 470, 720)},
    {"voce": "Lui è seduto a tavola, il mento appoggiato alla mano. Sorride appena.",
     "da": (1080, 600, 680), "a": (1070, 600, 600)},
    {"voce": "È la tavola di Natale: sulla tovaglia, pane e pomodoro, e un fiasco di vino impagliato.",
     "da": (930, 900, 640), "a": (1280, 860, 640)},
    {"voce": "Il figlio, in ginocchio, è felice: il suo regalo è un gattino, dentro un sacco.",
     "da": (420, 1000, 680), "a": (400, 1010, 600)},
    {"voce": "Un alberello in vaso, con una stella cometa in cima.",
     "da": (690, 720, 640), "a": (650, 420, 600)},
    {"voce": "Il muro di fondo: pennellate di colore puro, verdi e blu, accostate come tessere.",
     "da": (720, 300, 640), "a": (1300, 260, 620)},
    {"voce": "Maurizio Bertino ha voluto fermare qui la vita di famiglia, semplice e povera, di un tempo oramai passato.", "da": (1100, 646, 1100), "a": INTERO},
    {"voce": "Il quadro si chiama Tempi remoti. È del millenovecentonovantasette.",
     "sott": "Il quadro si chiama Tempi remoti. È del 1997.", "da": (1280, 1000, 640), "a": (1300, 1000, 600)},
    {"voce": "Lo trovate su arte maurizio bertino punto com.", "sott": "Lo trovate su artemauriziobertino.com",
     "da": INTERO, "a": (800, 646, 1520)},
]

# Musica: Eleven Music v2.5, strumentale, 72 s, generata il 29/10 (pianoforte e archi, lenta; quella del 28/10 durava 52 s)
MUSICA = os.path.join(QUI, "2026-10-29 Musica documentario - ElevenLabs.mp3")
VOL_MUSICA = 0.18      # circa 15 dB sotto la voce

# Suoni (ElevenLabs, effetti sonori v3, 29/10). Volumi tarati sulla media misurata: voce circa -20 dB,
# fuoco sotto tutto il reel circa -40 dB, effetti puntuali fra -30 e -35 dB.
E = os.path.join(QUI, "effetti")
AMBIENTE = [(os.path.join(E, "2026-10-29 Fuoco del camino - ElevenLabs.mp3"), 4.0)]
EFFETTI = [   # file, volume, (scena, secondi dall'inizio della sua frase)
    (os.path.join(E, "2026-10-29 Ciocco che scoppietta - ElevenLabs.mp3"), 2.5, (2, 0.2)),
    (os.path.join(E, "2026-10-29 Fruscio del sacco - ElevenLabs.mp3"), 4.0, (6, 0.0)),
    (os.path.join(E, "2026-10-29 Miagolio di gattino - ElevenLabs.mp3"), 1.6, (6, 2.6)),
    (os.path.join(E, "2026-10-29 Risata di bambino - ElevenLabs.mp3"), 0.5, (7, -0.7)),
]
