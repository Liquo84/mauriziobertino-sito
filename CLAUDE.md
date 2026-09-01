# Sito Maurizio Bertino

## Cos'è
Sito statico di `mauriziobertino.com`, ricostruito da zero per uscire da WordPress.
Solo HTML, CSS e un po' di JavaScript: niente database, niente abbonamento, niente aggiornamenti di sicurezza.
Vetrina delle opere di Maurizio: pittura (la sezione più ampia), scultura e riproduzioni di manufatti dei nativi d'America.

La guida completa in linguaggio non tecnico è in `LEGGIMI.md`: è scritta per Maurizio, non ripeterla qui.

## Obiettivo
Sostituire il sito WordPress. **Fatto**: il sito è online su GitHub Pages, si aggiorna da solo a ogni modifica caricata e non costa nulla.

**Il vecchio dominio non va più messo in sicurezza.** Il 21 agosto 2026 Davide e Maurizio hanno deciso di lasciare scadere `mauriziobertino.com` il 15 settembre: il sito faceva circa 300 visite l'anno e il rinnovo non valeva i ~15 €. Al suo posto registreranno **`artemauriziobertino.com`** con la promozione Aruba, ma solo *quando il sito sarà finito*.

Quando il nuovo dominio esiste: cambiare `DOMINIO` in `_backup-wp/genera.py`, rigenerare, aggiungere `sito/CNAME` e impostare il dominio in Settings → Pages.

## Vincoli e regole
- **Si pubblica solo la cartella `sito/`.** Il resto della cartella non va online.
- **`_backup-wp/` è archivio storico** dell'esportazione da WordPress: si consulta, non si modifica e non si pubblica.
- **Niente framework, niente CMS, niente database.** Il valore di questa ricostruzione è che resta un insieme di file.
- **Le foto originali stanno in un repository privato separato**, non in questo.
- **I testi pubblici sono concordati con Maurizio.** Non riscriverli di iniziativa: si propongono le modifiche e si aspetta l'ok.
- **I titoli delle opere sono di Maurizio.** Non si ribattezzano, non si traducono, non si "puliscono". Se un titolo manca si usa **"Senza titolo"**, convenzione già in uso nel catalogo, mai un titolo inventato. Vale anche per i termini scomodi ("mazza da guerra"): decisione presa il 30/08, non riaprirla.
- La pubblicazione è automatica via GitHub Pages, workflow `.github/workflows/pubblica.yml`.

## Dove stanno le cose
- `sito/` — il sito vero e proprio (home, opere, tecnica, nativi, diario, contatti, 404, articoli, assets, img).
- `immagini/` — immagini di lavorazione, fuori dal sito pubblicato.
- `_backup-wp/` — esportazione WordPress e script. `genera.py` costruisce il sito da `_catalogo.json`
  ed è quello che si lancia dopo ogni modifica; `aggiungi-opera.py` inserisce una nuova opera
  (anche con più viste, `--viste`); `estrai.py` e `catalogo.py` servirono solo all'importazione
  iniziale e **non vanno rilanciati** (catalogo.py si rifiuta da solo, per non perdere le opere
  aggiunte dopo).
- `social/` — piano editoriale e `genera-social.py`, che costruisce le immagini nei tre formati
  dalle foto del sito. Le immagini prodotte sono in `.gitignore`: si rigenerano con un comando.
- `LEGGIMI.md` — guida per Maurizio.
- `JOURNAL.md` — diario di lavoro.

## Come lavoriamo qui
- Il diario è in `JOURNAL.md`: leggilo in apertura di sessione, aggiornalo in chiusura.
- Le nuove opere si aggiungono con `aggiungi-opera.py`, non a mano nell'HTML.
- Ogni modifica ai testi visibili va segnalata a Maurizio prima di pubblicarla.
- **Sui social non si pubblica mai da qui.** Claude prepara immagini e didascalie, carica Davide a
  mano dopo l'ok di Maurizio. Decisione del 30/08, confermata il 01/09: l'account Instagram è
  personale e l'API non pubblicherebbe comunque.
