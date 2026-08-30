# JOURNAL — Sito Maurizio Bertino

Registro cronologico delle **decisioni** e di come sono andate.
Non è un elenco di cose fatte: serve a non ripetere gli errori e a non ridiscutere
scelte già prese. Le regole stabili stanno in `CLAUDE.md`, non qui. Qui c'è la storia.

Voce nuova in cima. Formato: **cosa**, **perché**, **esito** (aggiornato dopo).

**Ciclo:** si legge all'inizio (bastano stato + questioni aperte) → si lavora →
**si scrive nel momento in cui la decisione viene presa**, non a fine giornata.

---

## Stato al 30/08/2026

| | |
|---|---|
| Sito | Ricostruito e completo: 42 opere con filtri, 9 schede, tutte le pagine |
| Ultimo lavoro | 21/08 — nuova copertina e revisione testi con Maurizio |
| Pubblicazione | GitHub Pages, workflow `pubblica.yml` |
| **Dominio** | Registrato presso Automattic, **scade il 15/09/2026** |

Il nodo non è più il sito, è il dominio. Con due settimane di margine, la decisione va presa **entro il 01/09/2026**.

**Non contato:** se il sito sia già online e verificato non è deducibile dalla cartella. <!-- DA CONFERMARE -->

---

## Questioni aperte

- [ ] **Dominio: trasferire o tenere solo la registrazione** — trasferire a un registrar indipendente (10-12 €/anno, aggiunge un anno, chiude con WordPress) oppure disdire solo l'hosting restando clienti Automattic. Decisione entro il 01/09.
- [ ] **Verifica del sito online** — va fatta prima di toccare il dominio, non dopo.
- [ ] **Disdetta del piano WordPress** — ultimo passo, solo a dominio messo in sicurezza.

---

## 30/08 — Introdotti CLAUDE.md e JOURNAL.md

**Cosa.** Aggiunti i due file di memoria del progetto.
**Perché non basta il LEGGIMI.** Il `LEGGIMI.md` è scritto per Maurizio e spiega il progetto a chi lo apre; non dice a che punto siamo né perché abbiamo scelto una strada. Il `CLAUDE.md` rimanda al LEGGIMI invece di copiarlo, così non esistono due verità che divergono.

## 21/08 — I testi pubblici non si toccano senza l'ok di Maurizio

**Cosa.** Nuova copertina e revisione dei testi fatta insieme a Maurizio; corretta la frase sulle riproduzioni ("vestigia" rimosso).
**Perché la regola.** Il sito parla a nome suo. Una modifica ragionevole ma non concordata è comunque una modifica non sua.
**Esito.** Testi approvati e in linea.

## 21/08 — Ordine operativo del passaggio da WordPress

**Cosa.** Fissata la sequenza: pubblica il sito nuovo → verifica → sposta il dominio → ricontrolla → solo allora disdici WordPress.
**Perché quest'ordine e non un altro.** Toccare il dominio prima che il sito nuovo funzioni significa poter restare senza né l'uno né l'altro. E a ridosso della scadenza i trasferimenti possono fallire, quindi il margine va preso prima.

## 18/08 — Le opere si aggiungono con lo script, non a mano

**Cosa.** Aggiunte due opere ("La più bella del mondo", cavallo rampante) con `aggiungi-opera.py`; documentato lo script e aggiornati i conteggi.
**Perché.** Scrivere l'HTML a mano fa divergere catalogo, filtri e conteggi. Con lo script restano allineati.
**Esito.** 42 opere a catalogo, conteggi coerenti.

## 16/08 — Ricostruzione in HTML statico invece di un altro CMS

**Cosa.** Sito rifatto da zero in HTML, CSS e poco JavaScript; pubblicazione su GitHub Pages; foto originali in un repository privato separato.
**Perché lo statico e non una migrazione.** Un altro CMS avrebbe spostato il problema: abbonamento, database, aggiornamenti di sicurezza. Restano solo file: niente costi ricorrenti, niente manutenzione obbligata.
**Nota tecnica.** Si pubblica solo la cartella `sito/`. `_backup-wp/` è l'esportazione storica: si consulta, non si pubblica.
