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
| Sito | Online e verificato. 46 opere con filtri, 7 pagine, 9 articoli |
| Indirizzo | https://liquo84.github.io/mauriziobertino-sito/ |
| Pubblicazione | Automatica a ogni modifica caricata su GitHub |
| Dominio | Il vecchio si lascia scadere il 15/09. Il nuovo si compra a sito finito |
| Costo | Zero, finché non si registra il dominio |

Il sito non è più il nodo: è finito e funziona anche da telefono. Quello che manca
sono i dati delle opere, e dipende da Maurizio.

**Non contato:** le 46 opere includono **quattro pubblicate con titolo provvisorio
"Senza titolo"**, senza misure e (tranne il gufo) senza anno. Il conteggio le tratta
come le altre, ma le schede sono incomplete. Restano in archivio, non pubblicati,
lo scatto di taglio del cavallo e le due tracce audio del vecchio sito.

---

## Questioni aperte

- [ ] **Titoli e misure delle quattro opere nuove** — sono online come "Senza titolo": cinque opere del catalogo portano ora la stessa etichetta. Maurizio è lento a dare i dati, ma finché non arrivano il catalogo resta ambiguo.
- [ ] **Materiale delle due sculture in pietra** — sul sito è scritto genericamente "pietra". Se è pietra leccese va specificato: è un dato che qualifica l'opera.
- [ ] **Anno del dipinto con il viale di alberi** — la firma porta due cifre illeggibili alla risoluzione disponibile. Serve la conferma di Maurizio, non una supposizione.
- [ ] **Installare ffmpeg** — non c'è sulla macchina (Homebrew sì). Senza, sul video non si fa niente. Con, si generano video da catalogo senza girare nulla: 46 opere, 46 video. Domanda posta il 30/08, rimasta senza risposta.
- [ ] **Instagram: account Business o personale?** — con un profilo personale l'API non pubblica, e comunque il nome utente serve subito perché sul sito Instagram non c'è ancora.
- [ ] **Registrare artemauriziobertino.com** — da fare a sito finito. Prima di comprare, controllare il prezzo di rinnovo dal secondo anno: le promozioni a 1 € valgono il primo.
- [ ] **Disdetta del piano WordPress** — ultimo passo, quando il nuovo dominio è attivo.

---

## 30/08 — I social si preparano, non si automatizzano

**Cosa.** Per Facebook e Instagram si va di "livello 1": Claude prepara tutto (immagini nei tre formati, didascalie separate per le due piattaforme, hashtag, calendario editoriale dal catalogo), Davide carica. Niente pubblicazione via API. Frequenza: una uscita a settimana.
**Perché non l'automazione, visto che le API sono gratuite.** Verificato: Meta e YouTube non fanno pagare le chiamate. Ma pubblicare su Instagram richiede la revisione dell'app da parte di Meta, indicata in una-quattro settimane per ciclo e spesso più cicli, con esito non garantito. Con un post a settimana l'automazione risparmia dieci minuti e costa un mese di pratiche. Il tempo vero sta nel preparare il contenuto, ed è lì che si interviene.
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
