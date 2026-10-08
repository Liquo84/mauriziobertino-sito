# JOURNAL — Sito Maurizio Bertino — archivio 2026

Lezioni controllate contro il CLAUDE.md il 08/10/2026.

Voci spostate intatte dal `JOURNAL.md` nella manutenzione dell'08/10/2026 (chiesta da Davide):
dal 17/09 all'avvio di agosto. Le voci recenti, lo Stato e le questioni aperte stanno nel `JOURNAL.md`.

---

## 17/09 — artemauriziobertino.com è online

**Cosa.** Chiuso il DNSSEC di Register.it, Davide ha messo i DNS: 4 record A verso GitHub e `www`
CNAME verso `liquo84.github.io`. Dominio impostato in Pages con `gh api`, pubblicato il commit con
canonical, sitemap e robots nuovi (workflow verde), certificato approvato per dominio e `www`
(scade il 16/12, GitHub lo rinnova da solo), HTTPS obbligatorio attivo.
**Verificato.** `https://artemauriziobertino.com/` risponde 200 con il canonical giusto; `http`,
`www` e il vecchio `liquo84.github.io/mauriziobertino-sito/` rimandano lì con un 301. Per questo i
post social già schedulati con il vecchio link funzionano lo stesso e non vanno toccati.
**Due inciampi del pannello Register.it.** Il `www` esisteva già (CNAME del parcheggio): va
modificato, aggiungerne un altro dà "duplicato". E il nome `@` non vuol dire dominio principale:
crea un sottodominio `@.artemauriziobertino.com`. Il nome va scritto per intero. Regola in CLAUDE.md.
**Nota tecnica.** Subito dopo, dal telefono "server non trovato": i resolver pubblici avevano in
cache la risposta vuota di quando i record A non c'erano (15 minuti, rinnovati anche dai controlli
fatti nel frattempo). `www` rispondeva già. Non si tocca niente, si aspetta.
**Da fare.** Confermare che dal telefono si apre (atteso dalle 15:20 del 17/09).
**Esito.** Dal telefono si apre: confermato da Davide il 22/09. Era solo la cache dei resolver.

## 16/09 — Il dominio nuovo è su Register.it, e il rinnovo non va lasciato partire

**Cosa.** Davide ha comprato `artemauriziobertino.com` su Register.it a 0,50 € il primo anno
(registrato il 15/09 alle 22:13 UTC, scade il 15/09/2027). `DOMINIO` in `genera.py` punta già al
nuovo indirizzo e le pagine sono rigenerate: cambiano solo canonical, `og:url`, sitemap e robots.
**Perché non Aruba.** La scelta si è spostata sul prezzo del primo anno. Il confronto del 15/09 ha
trovato il .com a 1 € + IVA su IONOS, 4,90 € su Register.it, 4,99 € + IVA su Aruba, 10,46 $ fisso su
Cloudflare. Davide ha trovato su Register.it un prezzo ancora più basso.
**Il rischio.** Il listino Register.it rinnova il .com a **58,50 € + IVA** l'anno. Rinnovo automatico
spento; a luglio-agosto 2027 si trasferisce su Cloudflare, dove il trasferimento include l'anno.
**Ordine dei passi.** Prima i DNS su Register.it (quattro A verso GitHub, `www` in CNAME verso
`liquo84.github.io`), poi dominio in Settings → Pages e pubblicazione insieme. Caricare prima il
canonical nuovo avrebbe indicato a Google la pagina di parcheggio di Register.it.
**Correzione.** CLAUDE.md diceva di aggiungere `sito/CNAME`: con un workflow di Actions GitHub lo
ignora, il dominio si imposta solo nelle impostazioni di Pages.
**Esito.** Seguito l'ordine dei passi: il dominio è online dal 17/09 e dal telefono si apre dal
22/09 (voci del 17/09 e del 22/09).

## 10/09 — "Due opere" erano due foto di un'opera che c'era già

**Cosa.** Maurizio ha mandato due scatti. Sembravano due opere nuove: erano la tela intera
e un dettaglio del falciatore della stessa opera, **"La falciatura del grano"**, che sta in
catalogo dal principio come scheda n. 13 — con misure (60×40 cm), data (10/03/1995) e tecnica
già a posto. Lo scatto d'insieme ha sostituito quello del 2021; il dettaglio è la seconda vista.
**Correzione mia.** L'avevo aggiunta come opera nuova, e per qualche minuto in catalogo ce ne
sono state due uguali. Me ne sono accorto perché la scheda mostrava misure e anno che non avevo
inserito io: erano quelli della scheda vera. La regola che ne esce: **prima di aggiungere
un'opera si cerca il titolo in `_catalogo.json`**, anche quando chi la manda la presenta come
nuova. `aggiungi-opera.py` controlla i doppioni sul nome del file, non sul titolo, e il nome
del file di una foto nuova non coincide mai.
**Nota tecnica.** La foto d'insieme era storta e con cornice e muro dentro l'inquadratura, mentre
tutte le altre del catalogo sono ritagliate sulla tela. È stata raddrizzata in prospettiva sui
quattro angoli della tela e portata a 3:2 esatto, che è il rapporto vero dell'opera: 60×40.
**Perché sostituire e non affiancare.** Lo scatto del 2021 era slavato, bluastro e a bassa
risoluzione (720×467). Tenere tutti e due voleva dire far scegliere al lettore quale delle due
è l'opera. La vecchia immagine resta nella cartella `img/`, non cancellata, solo non più usata.
**Esito.** Online e verificato: 46 opere (non 47), una sola scheda, badge "2 viste", la lente si
apre e il tasto avanti porta al dettaglio. Nessuno sbordamento né a 1280 né a 375px.

## 10/09 — Il dominio nuovo si compra più avanti, e il vecchio muore lo stesso

**Cosa.** Il check settimanale ha trovato che `mauriziobertino.com` — che scade il 15/09 e non
si rinnova — è ancora scritto dentro il sito nuovo in quattro punti che parlano ai motori di
ricerca: canonical di ogni pagina, `og:url`, `sitemap.xml` e `robots.txt`. Davide ha deciso di
comprare `artemauriziobertino.com` più avanti.
**Perché è un problema e non un dettaglio.** Il canonical dice a Google *qual è* la versione
buona di una pagina. Dal 16/09 tutte le pagine su GitHub Pages indicheranno un indirizzo che non
esiste più — e se qualcuno ricompra quel dominio, lo indicheranno a casa sua. In più oggi il
vecchio dominio serve ancora il WordPress originale: è contenuto doppio, ed è quello indicizzato.
**Cosa resta sul tavolo.** Il tampone è una riga: `DOMINIO` in `genera.py` che punta all'indirizzo
GitHub Pages, rigenerare e caricare. Non è stato fatto perché tocca il dominio, e il dominio passa
da Davide. Quando arriverà `artemauriziobertino.com` la riga si cambia comunque una volta sola.
**Esito.** Il tampone non è servito: il dominio nuovo è stato comprato il 15/09 e `DOMINIO` è
cambiato una volta sola, direttamente sul nuovo (voce del 16/09).

## 10/09 — Il primo blocco social funziona senza mani

**Cosa.** Le prime due uscite schedulate sono partite da sole: il 3/09 "Ho un sito nuovo 🎯"
(16 like, 1 commento) e il 10/09 "Lo Sguardo della Tigre" (9 like, 2 commenti). Il calendario
regge, restano il 17 e il 24.
**Nota tecnica.** Instagram si legge ancora da sloggato, ma non dal profilo: la griglia dei post
sì, i conteggi e i link della bio stanno solo dentro l'HTML della pagina. Facebook da sloggato
dà nome, "in breve" e il sito indicato, che è quanto basta per il check.
**Da non concludere adesso.** Due post non dicono niente sul registro che funziona: i numeri si
leggono il 28/09, come deciso.
**Esito (29/09).** Sono partite da sole anche la terza e la quarta: 4 uscite su 4, storie comprese.

## 01/09 — riepilogo dell'avvio social

Compresso il 30/09 (manutenzione chiesta da Davide): nove voci del 01/09, tutte con esito. Il testo
completo è nella storia git del file. Le lezioni sono verificate nel CLAUDE.md.

- **Il sito si carica senza chiedere, il resto no.** Le modifiche verificate (rigenerate con
  `genera.py`, niente che sbordi a 1280 e a 375px) vanno su GitHub senza domande; cancellare
  contenuti, toccare il dominio, scrivere a Maurizio e pubblicare sui social a suo nome restano da
  confermare. *Perché:* il push pubblica ma si annulla con un commit; le quattro eccezioni no.
  *Esito:* in uso da un mese senza incidenti.
- **Il sito rimanda ai social.** Icone di Instagram, Facebook e YouTube nel piede, più la scheda
  Instagram nei Contatti. *Perché:* chi arrivava da Google non trovava nessun canale. *Correzione
  mia:* icone fatte 21×21, portate a 44×44 (regola in CLAUDE.md). *Esito:* online dal 01/09.
- **Il profilo non è da avviare: ha già 33 post.** Il primo post diventa l'annuncio del sito, non
  una presentazione. *Esito:* uscito il 3/09; i link in bio li ha cambiati Davide (22/09).
- **Si parte con l'indirizzo GitHub e i testi social li approva Davide.** Il link sta solo nel testo
  e si cambia dopo; si pubblica su Facebook e Instagram; le didascalie non passano da Maurizio.
  *Esito:* link cambiato nei testi dal 24/09; la regola sulle didascalie è arrivata nel CLAUDE.md
  solo il 29/09.
- **Le prime quattro uscite mostrano le tre anime.** 3/09 sito nuovo, 10/09 Tigre, 17/09 Aquila,
  24/09 Arco corto, di giovedì. *Perché:* quattro dipinti di fila avrebbero raccontato solo un
  pittore. Il «far leggere le didascalie a Maurizio» è stato superato lo stesso giorno dalla
  decisione qui sopra. *Esito:* uscite tutte; copertura su Facebook 182, 55, 258, 49.
- **Il tono di voce si rileva, non si progetta.** Didascalie riscritte sui due registri di Maurizio
  (voce diretta; scheda con storia, prima persona, numero in chiusura, 📐 e 📩). Analisi in
  `social/TONO-DI-VOCE.md`. *Correzione mia:* i primi copy erano in terza persona, da museo (regola
  in CLAUDE.md). *Esito:* blocco 1 uscito e blocco 2 approvato sullo stesso tono.
- **Le immagini si generano da script, e ffmpeg non serve.** `social/genera-social.py`, tre formati,
  opera mai ritagliata, su fondo carta. *Perché:* ritagliare un dipinto ne rompe la composizione.
  *Esito:* otto uscite senza toccare lo script.
- **Il formato delle immagini è confermato.** Da lì in poi lo script non si tocca: le uscite si
  aggiungono a `social/uscite.json`.
- **Il consuntivo si mette in calendario prima del blocco dopo.** Evento il 28/09 per leggere i dati
  e preparare il blocco 2 del 1/10. *Esito:* fatto il 29/09 con tre screenshot di Meta; clic e DM
  per acquisto n/d. L'evento è stato rifatto uguale per il 26/10.

## 2026-08 — riepilogo del passaggio da WordPress

Compresso il 30/09 (manutenzione chiesta da Davide): dodici voci dal 16 al 30/08, tutte con esito
o superate. Il testo completo è nella storia git del file. Le lezioni sono verificate nel CLAUDE.md.

- **16/08 — HTML statico invece di un altro CMS.** Sito rifatto in HTML, CSS e poco JavaScript su
  GitHub Pages, foto originali in un repository privato. *Perché:* un altro CMS avrebbe spostato il
  problema (abbonamento, database, aggiornamenti). *Esito:* online dal 17/09 su
  `artemauriziobertino.com`, costo zero a parte il dominio.
- **18/08 — Le opere si aggiungono con lo script.** `aggiungi-opera.py`, mai HTML a mano, perché
  catalogo, filtri e conteggi restino allineati. *Esito:* conteggi sempre coerenti.
- **21/08 — Ordine del passaggio.** Pubblicare, verificare, poi il dominio, poi disdire WordPress.
  *Esito:* sito online; la parte sul dominio è superata dalla decisione qui sotto. La disdetta di
  WordPress è ancora aperta.
- **21/08 — I testi pubblici non si toccano senza l'ok di Maurizio.** Il sito parla a nome suo.
  *Esito:* testi approvati. Vale per il sito, non per le didascalie social (01/09).
- **21/08 — La musica del vecchio sito non torna.** Una traccia è un disco Virgin del 1994
  (copyright), dell'altra non si conosce l'esecuzione; i browser bloccano comunque l'autoplay.
  *Esito:* Davide ha lasciato perdere.
- **21/08 — Il vecchio dominio si lascia scadere.** Circa 300 visite l'anno non valevano il rinnovo.
  *Esito:* dominio nuovo comprato il 15/09 su Register.it, non su Aruba; il `sito/CNAME` previsto non
  serviva (16/09). Il vecchio risulta però rinnovato fino al 2027: questione aperta.
- **30/08 — I social si preparano, non si automatizzano.** Livello 1: Claude prepara, Davide carica.
  *Perché:* la revisione dell'app di Meta costa settimane per risparmiare dieci minuti a settimana.
  *Esito:* l'account è personale, l'API non pubblicherebbe comunque.
- **30/08 — Le opere senza titolo si pubblicano lo stesso,** come «Senza titolo», mai con titoli
  inventati; l'anno illeggibile si omette. *Esito (29/09):* tre su quattro risolte da Maurizio
  (*Presenze silenziose* 1996, *Orologio (Ercole)*, gufo unito); resta la figura di nativo.
- **30/08 — Un'opera può avere più viste** (`--viste`), per le sculture a tutto tondo.
  *Esito:* in uso su cavallo, figura in pietra e gufo.
- **30/08 — Il menu passa a scomparsa sotto i 960px,** aree toccabili almeno 44px, copertina leggera
  sui telefoni. *Esito:* niente sborda; prima schermata della home da 395 a circa 155 KB.
- **30/08 — Pagina biografica separata dalla home,** spostando i testi senza riscriverli.
  *Esito:* `biografia.html` online.
- **30/08 — Introdotti CLAUDE.md e JOURNAL.md,** con il CLAUDE.md che rimanda al LEGGIMI invece di
  copiarlo. *Esito:* in uso a ogni sessione.
