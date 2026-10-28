"""ElevenLabs per i reel di Maurizio (dal 28/10/2026): voce narrante da documentario.

La chiave è quella che usa già Diamond (Portachiavi, servizio diamond-elevenlabs): stesso account, piano
Creator di Davide. Non si stampa e non si scrive in nessun file.
Ogni frase generata si salva in cache/ (fuori da git): un testo già letto non si paga due volte.
"""
import hashlib, json, os, subprocess, urllib.request, urllib.parse
from pathlib import Path

QUI = Path(__file__).parent
CACHE = QUI / "cache"


def _chiave():
    return subprocess.run(["security", "find-generic-password", "-a", os.environ["USER"],
                           "-s", "diamond-elevenlabs", "-w"], capture_output=True, text=True,
                          check=True).stdout.strip()


def _get(percorso, **parametri):
    url = "https://api.elevenlabs.io" + percorso + ("?" + urllib.parse.urlencode(parametri) if parametri else "")
    req = urllib.request.Request(url, headers={"xi-api-key": _chiave()})
    return json.load(urllib.request.urlopen(req, timeout=60))


def voci_condivise(**filtri):
    return _get("/v1/shared-voices", **filtri)["voices"]


def leggi(testo, uscita, voce, modello="eleven_v4", impostazioni=None):
    """Legge il testo con la voce data in un mp3 (dalla cache se c'è). Torna il percorso."""
    chiave_cache = hashlib.sha1(json.dumps([voce, modello, testo, impostazioni], sort_keys=True).encode()).hexdigest()[:16]
    salvato = CACHE / voce / f"{chiave_cache}.mp3"
    if not salvato.exists():
        salvato.parent.mkdir(parents=True, exist_ok=True)
        corpo = {"text": testo, "model_id": modello}
        if impostazioni:
            corpo["voice_settings"] = impostazioni
        req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voce}",
                                     data=json.dumps(corpo).encode(),
                                     headers={"xi-api-key": _chiave(), "Content-Type": "application/json",
                                              "Accept": "audio/mpeg"})
        salvato.write_bytes(urllib.request.urlopen(req, timeout=120).read())
    Path(uscita).write_bytes(salvato.read_bytes())
    return uscita


def musica(prompt, uscita, secondi, modello="music_v2_5"):
    """Musica strumentale (Eleven Music v2.5, modello normale, non beta: pagina «Eleven Music», letta il 28/10)."""
    if Path(uscita).exists():
        return uscita
    corpo = {"prompt": prompt, "music_length_ms": int(secondi * 1000), "model_id": modello,
             "force_instrumental": True}
    req = urllib.request.Request("https://api.elevenlabs.io/v1/music", data=json.dumps(corpo).encode(),
                                 headers={"xi-api-key": _chiave(), "Content-Type": "application/json"})
    Path(uscita).write_bytes(urllib.request.urlopen(req, timeout=300).read())
    return uscita
