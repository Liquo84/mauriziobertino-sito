# Blog «Diario» — strada A, design corto
Data: 16/11/2026. **Stato: approvato da Davide il 16/11** («a, approvati tutti e due», design e bozza del bisonte). Realizzato lo stesso giorno: `_backup-wp/aggiungi-articolo.py`, campo `opera`, «Leggi l'articolo» nel visore di Opere, primo articolo sul bisonte.

## Decisioni di Davide (16/11)
- Strada A, «La scheda del giovedì»: «La a mi piace, inoltre possiamo fare degli articoli che descrivono le opere già pubblicate».
- Il nome resta **«Diario»**: «Diario mi piace».
- Approvazione: «Gli articoli li approvo io».
- Autore: Maurizio, «può essere Maurizio senza problemi».
- Da dove partire: «non lo so, vedi tu». La scelta qui sotto è di Claude, da confermare.

## Obiettivo
Un articolo di approfondimento sul sito per ogni opera del post del giovedì, più articoli su opere già pubblicate sul sito, così il link «🔗» dei post porta a una pagina vera. Criterio: a fine blocco 4 (da giovedì 26/11) ogni post del giovedì ha il suo articolo e i Contatti restano raggiungibili da ogni articolo.

## Cosa cambia per chi legge
- `diario.html` resta l'elenco, ordinato per data, con un filtro Pittura / Scultura / Nativi d'America quando gli articoli passano i 15.
- Ogni articolo è in prima persona di Maurizio (autore), ha foto, riga dati (tecnica, anno, misure) e un invito a scrivere dalla pagina Contatti; in fondo il rimando alla scheda dell'opera.
- Il titolo dell'opera resta quello di Maurizio.

## Cadenza e lavoro
- Un articolo a settimana, il giovedì, sull'opera del post. In più, quando c'è tempo, un articolo su un'opera già pubblicata sul sito (non c'è obbligo di cadenza).
- Davide: circa 15-20 minuti a settimana per leggere e approvare la parte nuova (il post è già approvato).
- Testi: li scrive il subagente `copywriter` dai fatti già nel progetto (`VOCE.md`, vecchi articoli, post approvati, catalogo), li rilegge a freddo una seconda istanza, Davide approva. Fatti nuovi su un'opera (storia, tecnica, misure) li dà Maurizio tramite Davide: senza, l'articolo resta corto e lo si dice.

## Lavoro tecnico (dopo il sì)
1. `_backup-wp/aggiungi-articolo.py`: aggiunge un articolo a `_catalogo.json` (campo `articoli`: slug, titolo, data, `cover`, `blocchi`), con controllo dei doppioni sullo slug e sul titolo, come `aggiungi-opera.py`.
2. Collegamento articolo-opera: campo `opera` nell'articolo (titolo dell'opera nel catalogo). `genera.py` lo usa per mettere «Leggi l'articolo» sulla scheda opera e il rimando in fondo all'articolo; oggi `collega_articolo` lo fa solo per i Nativi, sul titolo.
3. Filtro nel Diario per sezione, solo dopo 15 articoli (criterio: il 16° articolo).
4. Feed RSS: non richiesto, fuori scope.
5. Verifica come ogni modifica al sito: `genera.py`, a 1280 e a 375 px, `controlla-link.py`.

## Da dove si parte (scelta di Claude, da confermare)
Bisonte e mazza: i loro post su Facebook puntano già a una pagina «articolo» (testa-di-bisonte e mazza con testa in pietra). Il bisonte è pubblicato il 16/11. La mazza si fa nel check di lunedì 23/11 (Davide, 16/11: «Mettilo nella sessione della prossima settimana»).

## Fuori scope
Newsletter, commenti, un'altra lingua, articoli su temi che non sono opere, un nuovo design delle pagine.

## Rischi e criteri
- Fatti inventati: l'articolo contiene solo fatti con fonte; le frasi in più sono segnalate «da confermare con Maurizio». Criterio: ogni frase ha la fonte nel rapporto del copywriter.
- Il blog si ferma: il vecchio Diario si è fermato nel 2025 (9 articoli, 2 nel 2025). Criterio per riparlarne: due giovedì di fila senza articolo.
- Pagina dell'opera senza dati (misure, anno): l'articolo esce con la riga dati incompleta solo se Davide lo approva.

## Prossimo passo
Il sì di Davide su questo design e sulla bozza del bisonte; poi `aggiungi-articolo.py` e il collegamento articolo-opera, poi la pubblicazione.
