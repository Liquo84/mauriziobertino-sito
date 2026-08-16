#!/usr/bin/env python3
"""Server di anteprima locale del sito (solo per lo sviluppo)."""
import os, functools, http.server, socketserver

CARTELLA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sito")
CARTELLA = os.path.normpath(CARTELLA)
PORTA = 8777


class Gestore(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORTA),
                            functools.partial(Gestore, directory=CARTELLA)) as srv:
    print(f"Anteprima su http://localhost:{PORTA}  ({CARTELLA})", flush=True)
    srv.serve_forever()
