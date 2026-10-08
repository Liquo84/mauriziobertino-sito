# VOCE — Sito Maurizio Bertino

> Scheda del copywriter per questo progetto. La legge prima di scrivere qualunque testo.
> Ogni fatto ha una fonte. Se un fatto non è qui, non va nei testi: si chiede.
> Aggiornata: 2026-10-08

## Chi è
Maurizio Bertino dipinge a olio, scolpisce (terracotta, cartapesta, pietra leccese) e riproduce
manufatti dei nativi d'America. Il sito artemauriziobertino.com è la vetrina delle opere; chi è
interessato a un pezzo gli scrive.

**Tipo di voce:** artista artigiano, vetrina e vendita a privati

**Nome:** Maurizio Bertino. Sui social parla lui in prima persona; sul sito i testi storici sono in
terza persona («Bertino», «l'Artista»).

## Chi legge
Privati che arrivano dai social o dal passaparola, curiosi delle opere, alcuni interessati a
comprare un pezzo unico. Non sono critici d'arte.

## Tono
- **Persona:** sui social prima persona di Maurizio; sul sito titoli e etichette neutri.
- **Registro:** artigiano che racconta e vende, non didascalia da museo (`social/TONO-DI-VOCE.md`).
- **Suona così:**
  - «Pezzo unico. Non ne esiste un altro uguale.» (Instagram, rilevato 01/09/2026)
  - «Ho voluto fermare quel momento in terracotta.» (Instagram)
- **Non suona così:**
  - «Maurizio la prepara e poi ci dipinge sopra» (terza persona da catalogo, scartata il 01/09)

## Parole
- **Da usare:** «pezzo unico», «Unici» (con la maiuscola, nella sua formula «regali Unici a persone Uniche»).
- **Vietate:** nessuna oltre al radar.
- **Nomi fissi:** le sezioni del sito sono «Pittura di fantasia» (scelto da Davide l'08/10, in
  attesa dell'ok di Maurizio; prima «La pittura»), «La scultura», «Nativi d'America»;
  filtri della pagina Opere: Tutte, Pittura, Scultura, Nativi d'America (`genera.py`, righe 423-426).

## Banca fatti
| Fatto | Fonte |
|---|---|
| Nato a Bienne (Svizzera) nel '65, scuole a Lausanne fino a 10 anni, poi in Italia | `sito/biografia.html` |
| Autodidatta, senza studi accademici | `sito/biografia.html` |
| «Un'arte Espressionista e non Accademica», paesaggi di fantasia, l'emozione dell'istante | `sito/tecnica.html` |
| Soggetti principali: la Natura e gli Animali | `sito/biografia.html` |
| Quadri: olio su tela, iuta, faesite; paesaggi, animali, nature morte | home, riquadro «La pittura» |
| 45 opere a catalogo: 25 nella sezione pittura (di cui 3 disegni), 11 sculture, 9 riproduzioni native | `_backup-wp/_catalogo.json`, letto il 08/10/2026 |
| I quadri li inventa dal nulla, e vuole che risalti questo; propone «fantasie dipinte» | Maurizio, riferito da Davide il 08/10/2026 |
| *Mah-to-toh-pa* (2004, china) riprende il ritratto di Mató-Tópe di Karl Bodmer (1834): non è inventato | confronto fatto il 08/10/2026 |
| Primo premio «Fare Naif Oggi» a Lerici | `sito/biografia.html` |

**Fatti mancanti (segnaposto in uso):**
- `[IN VENDITA?]` — quali dipinti sono ancora disponibili: lo sa Maurizio.

## Regole speciali del progetto
- I testi del sito sono concordati con Maurizio: si propongono, lui approva.
- I titoli delle opere sono suoi e non si toccano.
- Didascalie social: le approva Davide (CLAUDE.md del progetto).
- Collaudo alla cieca: Davide ha detto sì (08/10/2026) per la prima riscrittura di una pagina intera.

## Correzioni di Davide
- 2026-10-08 — «fantasie dipinte» non lo convince come espressione: cercare alternative che
  portino lo stesso concetto (quadri inventati dal nulla).
