# -*- coding: utf-8 -*-
"""Reel di prova «Tempi remoti» (28/10/2026). Testo della voce: scritto e rivisto dal copywriter il 28/10
(VOCE.md, eccezione dei reel «tipo Superquark»). Dati dell'opera: Maurizio, chat del 24/10.
Inquadrature: (centro x, centro y, larghezza) in pixel della foto 1600×1293; mai sotto 600 di larghezza.
"""
import os
QUI = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.abspath(os.path.join(QUI, "..", "..", ".."))
FOTO = os.path.join(PROG, "immagini", "tempi-remoti.JPG")
USCITA = os.path.join(QUI, "2026-10-28 Reel prova - Tempi remoti.mp4")

VOCE = "HuK8QKF35exsCh2e7fLT"          # Carmelo La Rosa, voce italiana già nell'account (libreria ElevenLabs)
IMPOSTAZIONI = {"stability": 0.6, "similarity_boost": 0.75, "speed": 0.92}
CODA = 2.5                             # secondi di cartello finale dopo l'ultima frase
CHIUSURA = ("Tempi remoti", "Maurizio Bertino, 1997")
CHIUSURA_DA = 10                       # dalla frase del titolo il cartello prende il posto dei sottotitoli

INTERO = (800, 646, 1600)
SCENE = [
    {"voce": "Una cucina di campagna, dipinta a olio.", "da": INTERO, "a": (800, 646, 1450)},
    {"voce": "Il camino acceso, la fiamma alta. Sopra, una treccia d'aglio.",
     "da": (330, 760, 660), "a": (320, 360, 620)},
    {"voce": "Una donna anziana, col fazzoletto azzurro, tiene le mani sulle spalle di un uomo.",
     "da": (1060, 250, 640), "a": (1090, 470, 720)},
    {"voce": "Lui è seduto a tavola, il mento appoggiato alla mano.",
     "da": (1080, 600, 680), "a": (1070, 600, 600)},
    {"voce": "Sulla tovaglia, pane spezzato e un fiasco impagliato.",
     "da": (930, 900, 640), "a": (1280, 860, 640)},
    {"voce": "A terra, un bambino in ginocchio sistema un cesto.",
     "da": (420, 1000, 680), "a": (400, 1010, 600)},
    {"voce": "Un alberello in vaso, con una stella in cima.",
     "da": (690, 720, 640), "a": (650, 420, 600)},
    {"voce": "Il muro di fondo: piccole pennellate verdi e blu, come tessere.",
     "da": (720, 300, 640), "a": (1300, 260, 620)},
    {"voce": "Maurizio Bertino inventa i suoi quadri dal nulla.", "da": (1100, 646, 1100), "a": INTERO},
    {"voce": "Il quadro si chiama Tempi remoti. È del millenovecentonovantasette.",
     "sott": "Il quadro si chiama Tempi remoti. È del 1997.", "da": (1280, 1000, 640), "a": (1300, 1000, 600)},
    {"voce": "Lo trovate su arte maurizio bertino punto com.", "sott": "Lo trovate su artemauriziobertino.com",
     "da": INTERO, "a": (800, 646, 1520)},
]

# Musica: Eleven Music v2.5, strumentale, 52 s, generata il 28/10 (pianoforte e archi, lenta)
MUSICA = os.path.join(QUI, "2026-10-28 Musica documentario - ElevenLabs.mp3")
VOL_MUSICA = 0.18      # circa 15 dB sotto la voce
