# Controllo dei link del check del lunedì: percorre il sito online e conta pagine, risorse e link esterni.
# Uso: /opt/homebrew/bin/python3 _backup-wp/controlla-link.py
import re, urllib.request, urllib.parse, sys
BASE="https://artemauriziobertino.com/"
def get(u, head=False):
    req=urllib.request.Request(u, method="HEAD" if head else "GET", headers={"User-Agent":"Mozilla/5.0 controllo-link"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r: return r.status, (r.read().decode("utf-8","ignore") if not head else "")
    except urllib.error.HTTPError as e: return e.code, ""
    except Exception as e: return str(e), ""
pages, seen, todo, res, ext = set(), set(), [BASE], set(), set()
while todo:
    u=todo.pop()
    if u in pages: continue
    pages.add(u); st, html = get(u)
    if st!=200: print("PAGINA", st, u, flush=True); continue
    for m in re.findall(r'(?:href|src)=["\']([^"\'#]+)', html):
        a=urllib.parse.urljoin(u,m)
        if a.startswith(("mailto:","tel:","javascript:")): continue
        if a.startswith(BASE):
            if a.endswith(".html") or a.endswith("/"): todo.append(a)
            else: res.add(a)
        elif a.startswith("http"): ext.add(a)
bad=[]
for a in sorted(res):
    st,_=get(a, head=True)
    if st!=200: bad.append((st,a))
for a in sorted(ext):
    st,_=get(a, head=True)
    if st not in (200,301,302,303,307,308,405,403): bad.append((st,a))
    print("ESTERNO", st, a, flush=True)
print(f"{len(pages)} pagine, {len(res)} risorse, {len(ext)} link esterni; non a posto: {len(bad)}")
for b in bad: print("  ", b)
