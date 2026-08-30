# Sito di Maurizio Bertino — versione statica

Ricostruzione completa di `mauriziobertino.com` senza WordPress.
Niente abbonamento, niente database, niente aggiornamenti di sicurezza: solo file.

---

## Il dominio: cosa è stato deciso

Il vecchio indirizzo `mauriziobertino.com` era registrato presso **Automattic**
(la società di WordPress.com) e **scade il 15 settembre 2026**.

**Decisione presa il 21 agosto 2026: lo si lascia scadere.** Il sito faceva circa
300 visite l'anno e il rinnovo non vale i ~15 €. Al suo posto verrà registrato
**`artemauriziobertino.com`** con la promozione Aruba, ma solo *quando il sito
sarà finito*.

Due cose da tenere a mente:

- **Controlla il prezzo di rinnovo prima di comprare.** Le promozioni a 1 € valgono
  quasi sempre solo il primo anno.
- **Alla scadenza il vecchio indirizzo diventa di chiunque.** Rischio basso con
  questi numeri, ma vuol dire che un domani `mauriziobertino.com` potrebbe mostrare
  qualcos'altro.

Fino ad allora il sito vive sull'indirizzo GitHub qui sotto, che funziona benissimo
e non costa nulla.

---

## Cosa c'è in questa cartella

```
mauriziobertino-sito/
├── sito/              ← IL SITO. È solo questa cartella che va pubblicata.
│   ├── index.html         Home
│   ├── opere.html         Catalogo, 46 opere con filtri
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
├── immagini/          ← Le 109 foto ORIGINALI a piena risoluzione (73 MB).
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

**Da pubblicare: solo il contenuto della cartella `sito/`.** Pesa circa 57 MB.

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
— 109 immagini a piena risoluzione, visibili solo a te.

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

## Collegare il nuovo dominio

Da fare quando `artemauriziobertino.com` sarà registrato. Tre passaggi.

**1. Nel pannello DNS di Aruba**, questi record:

| Tipo | Nome | Valore |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | liquo84.github.io |

**2. Un file `CNAME`** dentro la cartella `sito/`, contenente solo la riga
`artemauriziobertino.com`. E nel generatore va cambiata la costante `DOMINIO`,
così gli indirizzi dichiarati ai motori di ricerca si allineano.

**3. Nel repository**: *Settings → Pages → Custom domain*, scrivi
`artemauriziobertino.com` e spunta *Enforce HTTPS* (il certificato arriva da solo,
può volerci qualche ora).

I passaggi 2 e 3 li posso fare io. Il primo dipende dal pannello Aruba.

---

## Come aggiungere una nuova opera

Un comando solo. Pensa lui a tutto: archivia l'originale, crea le due versioni
per il web, inserisce la scheda in catalogo e rigenera le pagine.

```bash
python3 /Users/davideliquori/Desktop/mauriziobertino-sito/_backup-wp/aggiungi-opera.py ~/Downloads/FOTO.jpg --sezione pittura --titolo "Titolo dell'opera" --misure "50x40" --anno 2024 --tecnica "Olio su tela"
```

`--sezione` accetta `pittura`, `scultura` o `nativi`.
`--misure`, `--anno` e `--tecnica` sono facoltativi: se un dato non c'è, la scheda
semplicemente non lo mostra. Aggiungi `--nome-file "nome-pulito"` se la foto ha un
nome incomprensibile (tipo quelli scaricati da Facebook).

**Più foto della stessa opera.** Le sculture hanno bisogno di essere viste da più
lati. Basta elencare le altre foto dopo `--viste`:

```bash
python3 /Users/davideliquori/Desktop/mauriziobertino-sito/_backup-wp/aggiungi-opera.py ~/Downloads/FRONTE.jpg --sezione scultura --titolo "Titolo" --viste ~/Downloads/LATO.jpg ~/Downloads/RETRO.jpg
```

La prima foto è quella che appare nella griglia; sopra compare una piccola
etichetta "3 viste". Chi ingrandisce l'opera scorre le viste una dopo l'altra
con le frecce o col dito, e solo alla fine passa all'opera successiva.

Poi pubblica:

```bash
git add -A && git commit -m "nuova opera" && git push
```

E salva l'originale nella copia di sicurezza:

```bash
cd /Users/davideliquori/Desktop/mauriziobertino-sito/immagini && git add -A && git commit -m "nuova foto" && git push
```

---

## Cosa è cambiato rispetto al vecchio sito

**Tenuto tutto il contenuto**: le 40 opere del vecchio sito con titoli, misure,
anni e tecniche, le 14 schede delle riproduzioni native, i 9 articoli, la
biografia, la rassegna stampa e l'elenco delle mostre.

Il catalogo oggi conta **46 opere**: 25 dipinti, 12 sculture e 9 riproduzioni.

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
è ancora `mauriziobertino.com`, che è il vecchio dominio in scadenza. Va cambiato
in `artemauriziobertino.com` quando lo registrerete: è una riga sola nel generatore
(`DOMINIO`). Nel frattempo non fa danni: l'indirizzo GitHub funziona comunque.

---

## Manutenzione

Nessuna. Non c'è un database da aggiornare né plugin da tenere aggiornati.
I file restano identici finché non li cambi tu.
