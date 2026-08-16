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
│                        Copia di sicurezza: non serve pubblicarle, ma non buttarle.
│
├── _backup-wp/        ← Il "cantiere": copia delle vecchie pagine WordPress
│                        e gli script che hanno ricostruito il sito.
│                        Non va pubblicato.
│
└── LEGGIMI.md         ← questo file
```

**Da pubblicare: solo il contenuto della cartella `sito/`.** Pesa circa 56 MB.

---

## Cosa manca ancora (3 dati)

Nel file `_backup-wp/genera.py`, in cima, c'è questo blocco:

```python
CONTATTI = {
    "email": "mauriziobertinoartista@gmail.com",
    "whatsapp": "39XXXXXXXXXX",        # ← numero personale di Maurizio
    "instagram": "https://instagram.com/",   # ← link al profilo vero
    "facebook": "https://facebook.com/",     # ← link al profilo vero
}
```

- **WhatsApp**: numero in formato internazionale, senza `+` e senza spazi.
  Esempio: `393331234567`.
- **Instagram / Facebook**: i link ai profili veri.
  Nota: anche sul vecchio sito WordPress questi due link erano rotti, puntavano
  alle home di Instagram e Facebook invece che ai profili di Maurizio.

Dopo averli sistemati, rigenera il sito:

```bash
python3 /Users/davideliquori/Desktop/mauriziobertino-sito/_backup-wp/genera.py
```

---

## Come pubblicarlo (senza pagare)

Tutte e tre le opzioni sono gratuite per un sito come questo.

### Netlify — la più semplice

1. Vai su [app.netlify.com/drop](https://app.netlify.com/drop)
2. Trascina la cartella `sito` nella pagina.
3. Il sito è online in pochi secondi su un indirizzo tipo `xyz.netlify.app`.
4. Per usare `mauriziobertino.com`: *Domain settings → Add custom domain*, e poi
   punti lì i nameserver del dominio.

### Cloudflare Pages — la più veloce

1. Account gratuito su [dash.cloudflare.com](https://dash.cloudflare.com)
2. *Workers & Pages → Create → Pages → Upload assets*, carichi la cartella `sito`.
3. Se sposti anche il dominio su Cloudflare Registrar, gestisci tutto da un posto solo.

### GitHub Pages — se vuoi tenere la cronologia delle modifiche

1. Crei un repository, ci metti dentro il contenuto di `sito/`.
2. *Settings → Pages → Deploy from branch*.
3. Per il dominio custom serve un file `CNAME` con dentro `mauriziobertino.com`.

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
- Il modulo di contatto (richiede un server). Sostituito da email, WhatsApp e social.
- I pulsanti "Mi piace" e la barra di WordPress.com.

---

## Manutenzione

Nessuna. Non c'è un database da aggiornare né plugin da tenere aggiornati.
I file restano identici finché non li cambi tu.
