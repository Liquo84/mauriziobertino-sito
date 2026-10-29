# Anteprima del sito prima di caricare una modifica

Spostata qui dal `CLAUDE.md` nella manutenzione del 29/10/2026, parola per parola.

La verifica prima di caricare: pagine rigenerate con `genera.py` e controllo che nulla sbordi né a 1280 né a 375px.
Per l'anteprima il pannello del browser non legge la Scrivania (404) e aperto come `file://` dà
misure false. Procedura verificata l'08/10, con la sessione partita da `~`:
1. `rsync -a --delete sito/ <scratchpad della sessione>/sito/`;
2. in `~/.claude/launch.json` (un `.claude/launch.json` nel progetto il pannello non lo vede) si
   aggiunge la voce `sito-maurizio`, cioè `python3 -m http.server 8766 --directory <scratchpad>/sito`
   con `"port": 8766`. La 8765 è occupata da un vecchio `recv.py` e non si tocca;
3. `preview_start` su `sito-maurizio`;
4. dopo ogni `genera.py` si rifà l'rsync e si ricarica la pagina;
5. a fine lavoro `preview_stop` e si toglie la voce, che punta a una scratchpad che muore con la sessione.
