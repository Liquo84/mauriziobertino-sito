# JOURNAL — Sito Maurizio Bertino

Registro cronologico delle **decisioni** e di come sono andate.
Non è un elenco di cose fatte: serve a non ripetere gli errori e a non ridiscutere
scelte già prese. Le regole stabili stanno in `CLAUDE.md`, non qui. Qui c'è la storia.

Voce nuova in cima. Formato: **cosa**, **perché**, **esito** (aggiornato dopo).

**Ciclo:** si legge all'inizio (bastano stato + questioni aperte) → si lavora →
**si scrive nel momento in cui la decisione viene presa**, non a fine giornata.

---

## Stato al 25/09/2026

| | |
|---|---|
| Sito | Online e verificato al check del 22/09. 46 opere con filtri, 7 pagine, 9 articoli. Nessun link rotto, workflow verde |
| Indirizzo | https://artemauriziobertino.com/ (HTTPS attivo; il vecchio indirizzo GitHub e `www` rimandano qui) |
| Pubblicazione | Automatica, si carica senza chiedere se verificato |
| Social | Instagram `@mauriziobertino_arte` (153 follower), Facebook "Spazio Arte Bertino" (163), dati del 22/09 |
| Uscite | 3/09, 10/09 e 17/09 uscite (il 17/09 il migliore: 27 reazioni e 10 commenti su Facebook). La 24/09 si verifica al consuntivo |
| Consuntivo | A calendario il 28/09 alle 16:00, insieme alla preparazione del blocco 2 |
| Dati da Maurizio | **PDF con foto e righe da compilare pronto il 25/09**, sulla Scrivania di Davide: lo manda lui |
| Dominio | `artemauriziobertino.com` online dal 17/09, scade il 15/09/2027. Il vecchio risulta rinnovato fino al 15/09/2027: da chiarire |
| Costo | Zero |

Il sito gira da solo. Tutto il lavoro rimasto è fuori dal sito e dipende da
Maurizio: i dati delle opere, cosa è in vendita, l'account WordPress. Da oggi
c'è un documento solo che raccoglie tutto.

**Non contato:** le 46 opere includono sempre **quattro schede con titolo
provvisorio "Senza titolo"**, e forse un doppione (il gufo, vedi questioni
aperte): se si conferma, le opere sono 45. Oltre a queste, 18 schede non hanno
misure, anno o tecnica. Restano in archivio, non pubblicati, lo scatto di taglio
del cavallo e le due tracce audio del vecchio sito.

---

## Questioni aperte

- [ ] **Titoli e misure delle quattro opere nuove** — sono online come "Senza titolo": cinque opere del catalogo portano ora la stessa etichetta. Maurizio è lento a dare i dati, ma finché non arrivano il catalogo resta ambiguo.
- [ ] **Il gufo "Senza titolo" del 2019 è forse il "Gufo in terracotta" (36 cm)** — trovato il 25/09 mettendo le foto affiancate: sembra lo stesso gufo, crudo in una e cotto nell'altra. È un'ipotesi e la domanda è nel PDF per Maurizio. Se lo conferma, le schede si uniscono (regola del 10/09) e il titolo e le misure ci sono già.
- [ ] **Materiale delle due sculture in pietra** — sul sito è scritto genericamente "pietra". Se è pietra leccese va specificato: è un dato che qualifica l'opera.
- [ ] **Anno del dipinto con il viale di alberi** — la firma porta due cifre illeggibili alla risoluzione disponibile. Serve la conferma di Maurizio, non una supposizione.
- [ ] **Quali opere del catalogo sono in vendita** — le schede di Maurizio finiscono sempre con «Per info e acquisto». Sui dipinti non lo sappiamo, quindi la chiamata all'acquisto per ora è solo sulle riproduzioni.
- [ ] **ffmpeg, solo se si vorranno i video** — non è installato e per il livello 1 non serve. Resta aperta solo se un giorno si vorranno Reel dal catalogo.
- [ ] **Il registro "scheda" funziona quanto quello diretto?** — sul profilo i video hanno sempre avuto più reazioni dei post fotografici. Se si conferma il 28/09, nel blocco 2 i due registri vanno alternati.
- [ ] **Trasferire il dominio prima della scadenza** — il 22/09 Davide ha detto che il rinnovo automatico di Register.it non è un problema: sulla carta collegata non ci sono mai soldi, quindi i 58,50 € + IVA non partono. Resta il rovescio: se non si trasferisce su Cloudflare entro luglio-agosto 2027, il 15/09/2027 il dominio scade e il sito sparisce dall'indirizzo.
- [ ] **Il vecchio `mauriziobertino.com` risulta rinnovato fino al 15/09/2027** — trovato al check del 22/09. Non si sa ancora se WordPress.com ha addebitato il rinnovo o se è solo il periodo di grazia dei .com. Conta perché si decide insieme alla disdetta del piano WordPress.
- [ ] **Disdetta del piano WordPress** — il dominio nuovo è attivo dal 17/09: è l'ultimo passo rimasto del passaggio.

---

## 25/09 — I dati si chiedono a Maurizio con un PDF illustrato, non con un messaggio

**Cosa.** Un PDF di 8 pagine (`2026-09-25 Dati da chiedere a Maurizio.pdf`, sulla Scrivania di
Davide) con la foto di ogni opera e le righe da compilare. Contiene le quattro "Senza titolo", le altre 18
schede incomplete, una griglia di quadri e sculture con «☐ in vendita» e le due domande su WordPress.
Davide aveva chiesto prima un messaggio WhatsApp, poi ha preferito il PDF.
**Perché con le foto.** Maurizio non riconosce un'opera da "il bassorilievo con il disco", e un
elenco di 20 domande in chat resta senza risposta. Col foglio può scrivere a mano e mandare una
foto, o rispondere a voce citando il numero della scheda.
**Nota tecnica.** Le foto sono quelle di `sito/img/full`, ridotte: il PDF pesa 1,5 MB e passa su
WhatsApp. Lo script è stato un lavoro di una volta e non è nel repository. Se serve rifarlo, si
riparte da `_catalogo.json`, perché l'elenco delle schede incomplete si ricava da lì.
**Da fare.** Quando arrivano le risposte: titoli e dati con `genera.py`, «Per info e acquisto»
sulle opere segnate, e unire le due schede del gufo se Maurizio conferma che è lo stesso.

## 22/09 — Check settimanale: sito sano, link in bio sistemati, il vecchio dominio non è morto

**Cosa.** Check del lunedì fatto il martedì. Sito: workflow verde, certificato valido fino al
16/12 (rinnovo automatico di GitHub), `http`, `www` e il vecchio indirizzo GitHub rimandano con un
301, 131 indirizzi controllati fra pagine, immagini e link esterni, nessuno rotto. Da Maurizio
nessun dato nuovo.
**Social.** Il post del 17/09 è uscito: Instagram conta 36 post (33 + le tre uscite del blocco),
Facebook lo mostra in cima con 27 reazioni, 10 commenti e 1 condivisione, più di tutte le uscite
precedenti. Follower: 153 su Instagram (fermi), 163 su Facebook (+2). I link in bio li ha
sistemati Davide: Facebook indica `artemauriziobertino.com`; su Instagram il sito è ora il link in
chiaro, però con l'indirizzo GitHub `liquo84.github.io/mauriziobertino-sito`, che rimanda al
dominio nuovo e quindi funziona.
**La sorpresa.** Il registro ufficiale dei .com (Verisign) dà `mauriziobertino.com` in scadenza il
**15/09/2027**, ultima modifica 16/09. Il registrar è ancora Automattic (WordPress.com) e la pagina
dice "This domain is parked". Due letture possibili, da non confondere con un fatto: WordPress.com
ha rinnovato addebitando la carta di Maurizio, oppure è il rinnovo d'ufficio del registro durante
il periodo di grazia, che sparisce se il registrar non paga. Si chiarisce solo dall'account
WordPress.com.
**Da fare.** Il 28/09 il consuntivo con i dati di Meta Business Suite: il 17/09 su Facebook è il
primo segnale che il registro "scheda" può funzionare, ma è un post solo.

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

## 10/09 — Il primo blocco social funziona senza mani

**Cosa.** Le prime due uscite schedulate sono partite da sole: il 3/09 "Ho un sito nuovo 🎯"
(16 like, 1 commento) e il 10/09 "Lo Sguardo della Tigre" (9 like, 2 commenti). Il calendario
regge, restano il 17 e il 24.
**Nota tecnica.** Instagram si legge ancora da sloggato, ma non dal profilo: la griglia dei post
sì, i conteggi e i link della bio stanno solo dentro l'HTML della pagina. Facebook da sloggato
dà nome, "in breve" e il sito indicato, che è quanto basta per il check.
**Da non concludere adesso.** Due post non dicono niente sul registro che funziona: i numeri si
leggono il 28/09, come deciso.

## 01/09 — Il sito si carica senza chiedere, il resto no

**Cosa.** Da oggi le modifiche al sito verificate si caricano su GitHub senza domande.
Restano da confermare ogni volta: cancellare contenuti, toccare il dominio, scrivere a Maurizio,
pubblicare sui social a suo nome. Scritto in `CLAUDE.md`.
**Perché distinguere invece di chiedere sempre o mai.** Su questo progetto caricare non è salvare:
il workflow pubblica da solo, quindi ogni push cambia ciò che vedono gli altri. Ma è anche
un'azione che si torna indietro con un commit, e chiedere ogni volta allungava il giro senza
aggiungere sicurezza. Le quattro eccezioni sono le cose che *non* si tornano indietro con un
commit: quelle continuano a passare da Davide.
**Nota tecnica.** «Verificate» vuol dire due cose precise: pagine rigenerate con `genera.py`,
e controllo che nulla sbordi né a 1280 né a 375px. Senza quelle, la regola non si applica.

## 01/09 — Il sito rimanda ai social, non solo il contrario

**Cosa.** Icone di Instagram, Facebook e YouTube nel piede di ogni pagina, e una scheda Instagram
in più nella pagina Contatti (`@mauriziobertino_arte`). Tutto da `genera.py`: `CONTATTI` ora
contiene anche `instagram`, e le tre icone stanno in `ICONE_SOCIAL` in cima al file.
**Perché in cima al file e non con le altre icone.** Il piede viene costruito nel modello di pagina,
molto prima del blocco che disegna la pagina Contatti dove stava il dizionario `SVG`. Invece di
duplicare i tracciati, `SVG` ora si aggiorna da `ICONE_SOCIAL`: una sola definizione per icona.
**Perché serviva.** Il flusso era a senso unico: i post mandano al sito, il sito non rimandava da
nessuna parte. Chi arrivava da Google usciva e basta. Instagram in particolare non compariva in
nessuna pagina, pur essendo il canale su cui si pubblica.
**Correzione mia.** Le avevo fatte 21×21: area toccabile sotto i 44px minimi fissati il 30/08.
Il riquadro ora è 44×44 con margini negativi da -11px che lo riassorbono, così il piede non cresce
in altezza e l'icona resta allineata al testo — a destra sul desktop, a sinistra da telefono.
**Esito.** Verificato a 1280 e a 375px: nessuno sbordamento orizzontale, le tre aree sono 44×44,
il piede resta alto 112px come prima, e a 1280 il bordo dell'ultima icona cade esattamente sul
margine del testo.
**Da fare.** Le modifiche sono solo in locale. Finché non si carica su GitHub, online non cambia niente.

## 01/09 — Il primo blocco è schedulato, il consuntivo è già a calendario

**Cosa.** Le quattro uscite e le quattro storie sono state schedulate da Davide su Meta Business
Suite. Il 28/09 alle 16:00 c'è un evento una tantum per leggere i risultati e preparare il blocco 2,
che parte il 1° ottobre.
**Perché il 28 e non dopo l'ultimo post.** Il blocco 2 parte giovedì 1 ottobre: se il consuntivo si
facesse a ottobre inoltrato la cadenza settimanale si spezzerebbe. Il 28 il post del 24 ha quattro
giorni di dati — pochi ma sufficienti a vedere se ha girato.
**Nota tecnica.** Esisteva già un ricorrente del lunedì alle 14:00 ("Check sito Maurizio Bertino +
aggiornamenti artista + social") che nella descrizione copre anche la schedulazione social. Il nuovo
evento non lo sostituisce: è una tantum, sul consuntivo. Se i due si pestano i piedi, il ricorrente
resta e questo si cancella.
**Da fare.** Portare in sessione i dati di Meta Business Suite: copertura, interazioni, clic sul
link, nuovi follower, e soprattutto se sono arrivati DM per acquisto.

## 01/09 — Le immagini piacciono, il formato è confermato

**Cosa.** Il design delle immagini (opera contenuta su fondo carta, caratteri e colori del sito,
blocco titolo solo nelle storie) è approvato e diventa lo standard per le uscite successive.
**Esito.** Confermato da Davide senza modifiche. `genera-social.py` non si tocca: le uscite nuove
si aggiungono a `social/uscite.json`.

## 01/09 — Il tono di voce non si inventa: era già lì

**Cosa.** Le quattro didascalie sono state riscritte da capo sul tono di voce reale di Maurizio,
rilevato leggendo i post pubblici di Instagram e la pagina Facebook. L'analisi sta in
`social/TONO-DI-VOCE.md` e va letta prima di scrivere qualsiasi testo social nuovo.
**Correzione mia.** I primi quattro copy li avevo scritti in terza persona, con tono da didascalia
di museo: titolo, tecnica, misure, punto. Davide li ha bocciati in blocco e ha avuto ragione.
Non avevo guardato che cosa il profilo pubblica già, avevo scritto quello che *sembrava giusto*
per un artista. La regola che ne esce: **quando un canale esiste già, il tono si rileva, non si
progetta** — e si rileva prima di scrivere, non dopo che il cliente ha detto che non gli piace.
**Cosa fa lui davvero.** Due registri. Uno breve ed esclamativo per i video ("Spoiler del nuovo
video 🤩🤩"). Uno a struttura fissa per le opere: una riga di storia che non nomina l'oggetto,
due paragrafi di contesto storico, lo scarto in prima persona ("Ho voluto fermare quel momento in
terracotta"), una chiusura con dentro un numero ("tremila anni di storia in 42 centimetri"), e in
fondo il blocco `📐 materiali | misure` più `📩 Per info e acquisto`. Vende, sempre.
**Nota tecnica.** Facebook è dietro login e non risulta un accesso attivo su Chrome: da lì si legge
solo la descrizione della pagina e il post in cima. Instagram invece si legge post per post da
sloggato, aprendo i permalink singoli. Se serviranno più dati, quella è la strada.

## 01/09 — Il profilo non è da avviare: ha già 33 post

**Cosa.** Instagram `@mauriziobertino_arte` ha 33 post e 154 follower, Facebook "Spazio Arte
Bertino" (`@mauriziobertinoartista`) ne ha 162. Di conseguenza il primo post non è più una
presentazione ma l'annuncio del sito nuovo.
**Perché cambiare il primo post.** Presentarsi a chi ti segue da mesi è una schermata sprecata.
Il sito online è una notizia vera per quel pubblico, e serve anche a giustificare il cambio del
link in bio.
**Nota tecnica.** Il link in bio di Instagram oggi porta a un video YouTube, e la pagina Facebook
indica ancora `mauriziobertino.com`, che scade il 15/09. Vanno cambiati tutti e due **prima** del
post del 3 settembre, altrimenti il primo post rimanda a un posto che non c'è.
**Da fare.** Cambiare i due link. È di Davide, non serve Maurizio.

## 01/09 — Si parte con l'indirizzo brutto, e i testi social li approva Davide

**Cosa.** Tre risposte che sbloccano l'avvio: il link nelle didascalie e in bio resta
`liquo84.github.io/mauriziobertino-sito/` e si cambia dopo; la pagina Facebook esiste, quindi si
pubblica su entrambi i canali; le didascalie social non passano da Maurizio, le approva Davide.
**Perché non aspettare il dominio, come avevo proposto.** Il link vive solo nel testo delle
didascalie, non dentro le immagini: cambiarlo dopo costa una sostituzione in un file. Rimandare
l'avvio dei social all'acquisto di un dominio sarebbe stato legare una cosa fatta a una cosa da
fare. La registrazione resta dov'era, in coda.
**Nota tecnica.** La regola dei testi concordati con Maurizio in `CLAUDE.md` riguarda i **testi del
sito** e non cambia. Le didascalie social sono materiale di Davide.

## 01/09 — Le prime quattro uscite mostrano le tre anime, non solo la pittura

**Cosa.** Calendario di avvio: 3/09 presentazione (Maurizio allo stand di Piacenza), 10/09 pittura
("Lo Sguardo della Tigre"), 17/09 scultura ("Aquila"), 24/09 nativi ("Arco corto delle pianure").
Una uscita a settimana, sempre di giovedì. Tutto in `social/PIANO.md`.
**Perché non partire dalla pittura, che è la sezione più ampia.** Un profilo nuovo si giudica dalle
prime schermate. Quattro dipinti di fila avrebbero raccontato un pittore, e il lavoro sui nativi —
che è la parte più insolita e quella che porta Maurizio alle fiere — sarebbe rimasta invisibile.
**Nota tecnica.** Le opere scelte hanno tutte un testo già scritto e verificato da cui partire
(articolo del sito o scheda di catalogo). Nessuna didascalia contiene un dato inventato: dove il
catalogo tace, il testo tace. L'"Arco corto" chiude il cerchio con la foto della fiera del primo post.
**Da fare.** Far leggere le quattro didascalie a Maurizio prima di caricare.

## 01/09 — Le immagini social si generano da script, e ffmpeg non serve

**Cosa.** `social/genera-social.py` costruisce i tre formati (1080×1080 Facebook, 1080×1350
Instagram, 1080×1920 storie) dalle foto già in `sito/img/full`. L'opera non viene mai ritagliata:
è contenuta su fondo carta, con lo stesso colore e lo stesso carattere del sito. Le immagini
prodotte sono in `.gitignore`: sono derivate, si rifanno con un comando.
**Perché uno script invece di ritagliare a mano volta per volta.** Ritagliare un'opera per farla
stare in un quadrato è la cosa peggiore che si possa fare a un dipinto: si perde la composizione,
che è metà del lavoro. Il fondo carta risolve il problema e per giunta fa somigliare il profilo al
sito. A mano, quarantasei opere per tre formati sono centotrentotto ritagli; con lo script sono
una riga di JSON per uscita.
**Perché ffmpeg non serviva.** La domanda del 30/08 dava per scontato che servisse: non è
installato e per le immagini statiche non c'entra nulla — basta PIL, che c'è già. Resta necessario
solo se un giorno si vorranno i video, e quella è una decisione separata.
**Nota tecnica.** L'arco corto è una foto molto stretta (687×1800): nel quadrato resta una fascia
verticale con molta carta intorno. Verificato a occhio, funziona — sembra una stampa su cartoncino,
non un errore. Se un giorno darà fastidio, per quel formato si userà una seconda vista.

## 30/08 — I social si preparano, non si automatizzano

**Cosa.** Per Facebook e Instagram si va di "livello 1": Claude prepara tutto (immagini nei tre formati, didascalie separate per le due piattaforme, hashtag, calendario editoriale dal catalogo), Davide carica. Niente pubblicazione via API. Frequenza: una uscita a settimana.
**Perché non l'automazione, visto che le API sono gratuite.** Verificato: Meta e YouTube non fanno pagare le chiamate. Ma pubblicare su Instagram richiede la revisione dell'app da parte di Meta, indicata in una-quattro settimane per ciclo e spesso più cicli, con esito non garantito. Con un post a settimana l'automazione risparmia dieci minuti e costa un mese di pratiche. Il tempo vero sta nel preparare il contenuto, ed è lì che si interviene.
**Esito (01/09).** Confermata dai fatti: l'account di Maurizio è **personale**
(@mauriziobertino_arte), e con un profilo personale l'API di Instagram non pubblica affatto.
La strada del livello 2 sarebbe stata chiusa in partenza, non solo lenta.
**Nota tecnica.** Claude non ha alcun connettore per Facebook, Instagram o YouTube: verificato nel registro, zero risultati. Il livello 2 richiederebbe token Meta generati da Davide e chiamate HTTP dirette. Resta la regola: niente pubblicazione a nome di Maurizio senza via libera esplicito, volta per volta.
**Da fare.** Il materiale si costruisce dal sito, che è già un archivio strutturato: 46 opere con foto, materiali e anni, più 9 articoli. Sono quasi un anno di uscite senza inventare niente.

## 30/08 — Le opere senza titolo si pubblicano lo stesso

**Cosa.** Le quattro opere nuove (dipinto del viale, figura di nativo in pietra, bassorilievo con il disco, gufo del 2019) sono online con titolo "Senza titolo". Confermato l'anno del gufo, 2019, leggendo la firma ingrandita.
**Perché pubblicare invece di aspettare.** Maurizio le vuole online e i dati non arrivano. "Senza titolo" non è un ripiego inventato: è convenzione d'arte, e il catalogo la usava già per un dipinto del 1997. Inventare un titolo sarebbe stato peggio del vuoto.
**Nota tecnica.** L'anno del dipinto è stato omesso: la firma porta due cifre che a quella risoluzione possono essere 96, 94 o 86. Meglio niente che una data sbagliata. I materiali sono dedotti dalle foto e vanno confermati.
**Da fare.** Sostituire i quattro titoli appena Maurizio li dà.

## 30/08 — Una pagina biografica separata dalla home

**Cosa.** La biografia, la rassegna stampa e le mostre escono dalla home e diventano `biografia.html`, con il ritratto di Maurizio accanto al gufo. La home resta corta e rimanda.
**Perché spostare e non duplicare.** Tenere gli stessi testi in due punti significa che prima o poi divergono. I testi non sono stati riscritti, solo spostati: la regola del 21/08 vale sul contenuto, non sulla collocazione.

## 30/08 — Un'opera può avere più viste

**Cosa.** Una scheda può portare più foto. Nella griglia compare "N viste", l'ingranditore le scorre prima di passare all'opera dopo. `aggiungi-opera.py` accetta `--viste`.
**Perché serviva davvero.** Le sculture a tutto tondo con una sola foto non si capiscono: per la figura in pietra Maurizio ha mandato quattro scatti proprio per questo.
**Esito.** Applicato a cavallo rampante, figura in pietra e gufo. I filtri continuano a funzionare: l'elenco si ricostruisce a ogni cambio.

## 30/08 — La soglia del menu sale a 960px

**Cosa.** Verifica su schermo da 375px. Corretti tre difetti: pulsanti sotto i 44px minimi, menu che andava a capo fra 861 e 959px, copertina scaricata a piena risoluzione anche sui telefoni.
**Perché la soglia e non un menu più stretto.** Con l'aggiunta di "Biografia" le voci sono sette e non stanno più su una riga sotto i 960px. Rimpicciolire il testo del menu avrebbe peggiorato la leggibilità: meglio passare prima al menu a scomparsa.
**Esito.** Nessuna pagina sborda in orizzontale, tutte le aree toccabili sono ≥44px, la prima schermata della home scende da 395 a circa 155 KB.

## 30/08 — Introdotti CLAUDE.md e JOURNAL.md

**Cosa.** Aggiunti i due file di memoria del progetto.
**Perché non basta il LEGGIMI.** Il `LEGGIMI.md` è scritto per Maurizio e spiega il progetto a chi lo apre; non dice a che punto siamo né perché abbiamo scelto una strada. Il `CLAUDE.md` rimanda al LEGGIMI invece di copiarlo, così non esistono due verità che divergono.

## 21/08 — Il vecchio dominio si lascia scadere

**Cosa.** `mauriziobertino.com` non verrà rinnovato: scade il 15/09/2026 e finisce lì. Al suo posto verrà registrato `artemauriziobertino.com` su Aruba, a sito finito.
**Perché lasciarlo andare invece di metterlo in sicurezza.** Il sito faceva circa 300 visite l'anno: spendere ~15 € l'anno per conservare un indirizzo con quel traffico non ha senso. Questa decisione **supera la parte sul dominio** della voce del 21/08 sull'ordine operativo, che dava per scontato di doverlo trasferire.
**Nota tecnica.** Registrata in ritardo nel diario: il 30/08 il journal è stato ricostruito dai file e riportava ancora la vecchia impostazione.
**Da fare.** Alla registrazione: cambiare `DOMINIO` in `genera.py`, aggiungere `sito/CNAME`, impostare il dominio in Settings → Pages.

## 21/08 — La musica del vecchio sito non torna online

**Cosa.** Le due tracce che partivano da sole (Mozart sulle Opere, Sacred Spirit sui nativi) sono state recuperate e archiviate nel repository privato, ma non ripubblicate.
**Perché non è una scelta di gusto.** La seconda è un disco Virgin del 1994: ripubblicarla è violazione di copyright, e il conto lo pagherebbe Maurizio. Della prima non si conosce l'incisione, e Mozart è di pubblico dominio ma le esecuzioni no. In più i browser bloccano l'audio automatico: anche sul vecchio sito, per quasi tutti, non partiva.
**Esito.** Davide ha lasciato perdere la musica.

## 21/08 — I testi pubblici non si toccano senza l'ok di Maurizio

**Cosa.** Nuova copertina e revisione dei testi fatta insieme a Maurizio; corretta la frase sulle riproduzioni ("vestigia" rimosso).
**Perché la regola.** Il sito parla a nome suo. Una modifica ragionevole ma non concordata è comunque una modifica non sua.
**Esito.** Testi approvati e in linea.

## 21/08 — Ordine operativo del passaggio da WordPress

**Cosa.** Fissata la sequenza: pubblica il sito nuovo → verifica → sposta il dominio → ricontrolla → solo allora disdici WordPress.
**Perché quest'ordine e non un altro.** Toccare il dominio prima che il sito nuovo funzioni significa poter restare senza né l'uno né l'altro. E a ridosso della scadenza i trasferimenti possono fallire, quindi il margine va preso prima.
**Esito.** Il sito è online e verificato. La parte sul dominio è superata dalla decisione del 21/08 di lasciarlo scadere: non c'è più niente da trasferire.

## 18/08 — Le opere si aggiungono con lo script, non a mano

**Cosa.** Aggiunte due opere ("La più bella del mondo", cavallo rampante) con `aggiungi-opera.py`; documentato lo script e aggiornati i conteggi.
**Perché.** Scrivere l'HTML a mano fa divergere catalogo, filtri e conteggi. Con lo script restano allineati.
**Esito.** 42 opere a catalogo, conteggi coerenti.

## 16/08 — Ricostruzione in HTML statico invece di un altro CMS

**Cosa.** Sito rifatto da zero in HTML, CSS e poco JavaScript; pubblicazione su GitHub Pages; foto originali in un repository privato separato.
**Perché lo statico e non una migrazione.** Un altro CMS avrebbe spostato il problema: abbonamento, database, aggiornamenti di sicurezza. Restano solo file: niente costi ricorrenti, niente manutenzione obbligata.
**Nota tecnica.** Si pubblica solo la cartella `sito/`. `_backup-wp/` è l'esportazione storica: si consulta, non si pubblica.
