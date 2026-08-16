# Sito di Maurizio Bertino — versione statica

Ricostruzione completa di `mauriziobertino.com` senza WordPress.
Niente abbonamento, niente database, niente aggiornamenti di sicurezza: solo file.

---

## ⚠️ Prima di disdire WordPress: il dominio

Il dominio **non è tuo su un registrar indipendente**. Risulta:

| | |
|---|---|
| Registrar | **Automattic Inc.** (la società di WordPress.com) |
| Nameserver | NS1/NS2/NS3.WORDPRESS.COM |
| Registrato il | 15 settembre 2021 |
| **Scadenza** | **15 settembre 2026** |

Tradotto: l'indirizzo `mauriziobertino.com` è gestito da WordPress. Se disdici tutto
senza toccare il dominio, rischi che alla scadenza l'indirizzo si liberi e chiunque
possa prenderlo. Chi cerca "Maurizio Bertino" su Google finirebbe altrove.

**Le due strade possibili:**

1. **Trasferire il dominio a un altro registrar** (Cloudflare Registrar, Namecheap,
   Gandi…). Si sblocca il dominio dal pannello WordPress.com, si chiede il codice di
   autorizzazione (AuthCode/EPP) e lo si usa sul nuovo registrar. Il trasferimento
   aggiunge un anno alla scadenza. Costo tipico: 10–12 € l'anno.
   È la strada giusta se vuoi chiudere del tutto con WordPress.

2. **Tenere solo la registrazione del dominio su WordPress.com** e disdire il piano
   di hosting. Cambi i nameserver puntandoli al nuovo hosting. Paghi solo il dominio.
   Più semplice, ma resti cliente Automattic.

**Non fare il trasferimento all'ultimo momento**: a ridosso della scadenza i
trasferimenti possono fallire. Muoviti con almeno due settimane di margine,
e comunque **solo dopo** che il nuovo sito è online e funzionante.

Ordine consigliato: pubblica il sito nuovo → verifica che funzioni → sposta il
dominio → controlla ancora → solo allora disdici il piano WordPress.

---

## Cosa c'è in questa cartella

```
mauriziobertino-sito/
├── sito/              ← IL SITO. È solo questa cartella che va pubblicata.
│   ├── index.html         Home
│   ├── opere.html         Catalogo, 40 opere con filtri
│   ├── tecnica.html       La tecnica
│   ├── nativi.html        La passione per i nativi d'America
│   ├── diario.html        Elenco delle schede
│   ├── contatti.html      Email, WhatsApp, social
│   ├── 404.html           Pagina di errore
│   ├── articoli/          9 schede di approfondimento
│   ├── assets/            stile.css e sito.js
│   ├── img/               copertina, miniature e immagini grandi
│   ├── robots.txt
│   └── sitemap.xml
│
├── immagini/          ← Le 107 foto ORIGINALI a piena risoluzione (73 MB).
│                        È un repository a sé, privato. Non finisce nel sito.
│
├── _backup-wp/        ← Il "cantiere": copia delle vecchie pagine WordPress
│                        e gli script che hanno ricostruito il sito.
│                        Non finisce online, ma è versionato su GitHub.
│
├── .github/workflows/ ← Pubblica il sito da solo a ogni modifica caricata.
│
└── LEGGIMI.md         ← questo file
```

**Da pubblicare: solo il contenuto della cartella `sito/`.** Pesa circa 56 MB.

---

## Il sito è già online

| | |
|---|---|
| Indirizzo provvisorio | **https://liquo84.github.io/mauriziobertino-sito/** |
| Repository | https://github.com/Liquo84/mauriziobertino-sito (pubblico) |
| Costo | zero |

I contatti sono già impostati: email, WhatsApp `331 438 5178`, la pagina Facebook
e il canale YouTube. Instagram e TikTok per ora non ci sono.

**Le foto originali stanno in un repository a parte, privato:**
[mauriziobertino-foto-originali](https://github.com/Liquo84/mauriziobertino-foto-originali)
— 107 immagini a piena risoluzione, visibili solo a te.

In questo repository pubblico ci sono solo le versioni ottimizzate per il web:
la cartella `immagini/` è esclusa apposta.

### Come si aggiorna

Ogni modifica caricata su GitHub viene pubblicata da sola, in un paio di minuti.
Dopo aver cambiato qualcosa (per esempio rigenerando con `genera.py`):

```bash
cd /Users/davideliquori/Desktop/mauriziobertino-sito && git add -A && git commit -m "descrizione della modifica" && git push
```

Per vedere il sito in locale prima di pubblicarlo:

```bash
cd /Users/davideliquori/Desktop/mauriziobertino-sito/sito && python3 -m http.server 8779
```

Poi apri `http://localhost:8779`.

---

## Collegare il dominio mauriziobertino.com

Da fare **solo dopo** aver sistemato la questione registrar qui sopra.
Sono tre passaggi.

**1. Nel pannello DNS del dominio**, questi record:

| Tipo | Nome | Valore |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | liquo84.github.io |

**2. Un file `CNAME`** dentro la cartella `sito/`, contenente solo la riga
`mauriziobertino.com`.

**3. Nel repository**: *Settings → Pages → Custom domain*, scrivi
`mauriziobertino.com` e spunta *Enforce HTTPS* (il certificato arriva da solo,
può volerci qualche ora).

Quando sei pronto chiedimi di farlo: sono operazioni che posso eseguire io,
tranne la modifica dei DNS che dipende da dove sta il dominio.

---

## Come aggiungere una nuova opera

Il sito è generato da uno script, ma puoi anche modificare l'HTML a mano.
Il modo pulito è passare dallo script:

1. Metti la foto nuova in `immagini/`.
2. Crea le due versioni per il web:

```bash
cd /Users/davideliquori/Desktop/mauriziobertino-sito
sips -s format jpeg -s formatOptions 80 -Z 1800 immagini/NOME.jpg --out sito/img/full/NOME.jpg
sips -s format jpeg -s formatOptions 60 -Z 640  immagini/NOME.jpg --out sito/img/thumb/NOME.jpg
```

3. Aggiungi la scheda dell'opera in `_backup-wp/_catalogo.json` (copia una voce
   esistente e cambia i campi) e rigenera con `genera.py`.

Se preferisci non toccare gli script, chiedi a Claude: la cartella `_backup-wp`
contiene tutto quello che serve per capire come è fatto.

---

## Cosa è cambiato rispetto al vecchio sito

**Tenuto tutto il contenuto**: le 40 opere con titoli, misure, anni e tecniche,
le 14 schede delle riproduzioni native, i 9 articoli, la biografia, la rassegna
stampa e l'elenco delle mostre.

**Migliorato:**
- Le opere si vedono in una griglia che rispetta le proporzioni dei quadri,
  con filtri per pittura / scultura / nativi.
- Click su un'opera per ingrandirla; frecce della tastiera o dito per scorrere.
- Layout pensato per il telefono: menu a scomparsa, griglia a una colonna,
  ingrandimento a schermo pieno con scorrimento a dito.
- Tema chiaro e scuro, si adatta alle preferenze di chi guarda.
- Immagini alleggerite: le miniature pesano circa la metà (56 KB in media).
- Le schede delle riproduzioni sono collegate ai relativi articoli.

**Tolto:**
- Il modulo di contatto (richiede un server). Sostituito da email, WhatsApp,
  Facebook e YouTube.
- I pulsanti "Mi piace" e la barra di WordPress.com.

**Da sapere:** nelle pagine, l'indirizzo "ufficiale" dichiarato ai motori di ricerca
è già `mauriziobertino.com`. È corretto per quando il dominio sarà collegato;
fino ad allora l'indirizzo GitHub funziona ma rimanda a quello come versione
principale.

---

## Manutenzione

Nessuna. Non c'è un database da aggiornare né plugin da tenere aggiornati.
I file restano identici finché non li cambi tu.
