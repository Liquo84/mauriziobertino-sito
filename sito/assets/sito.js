/* Maurizio Bertino — comportamenti del sito.
   Vanilla JS, nessuna dipendenza. */
(function () {
  "use strict";

  /* ---------- tema chiaro/scuro ---------- */
  var radice = document.documentElement;
  try {
    var salvato = localStorage.getItem("tema");
    if (salvato) radice.setAttribute("data-tema", salvato);
  } catch (e) { /* localStorage non disponibile: si usa il tema di sistema */ }

  document.addEventListener("click", function (ev) {
    var b = ev.target.closest(".tema-btn");
    if (!b) return;
    var scuroOra = radice.getAttribute("data-tema")
      ? radice.getAttribute("data-tema") === "scuro"
      : matchMedia("(prefers-color-scheme: dark)").matches;
    var nuovo = scuroOra ? "chiaro" : "scuro";
    radice.setAttribute("data-tema", nuovo);
    try { localStorage.setItem("tema", nuovo); } catch (e) {}
    b.setAttribute("aria-label", nuovo === "scuro" ? "Passa al tema chiaro" : "Passa al tema scuro");
  });

  /* ---------- menu mobile ---------- */
  var bottoneMenu = document.querySelector(".menu-btn");
  var menu = document.querySelector(".menu");
  if (bottoneMenu && menu) {
    bottoneMenu.addEventListener("click", function () {
      var aperto = menu.classList.toggle("aperto");
      bottoneMenu.setAttribute("aria-expanded", aperto ? "true" : "false");
    });
    menu.addEventListener("click", function (ev) {
      if (ev.target.tagName === "A") {
        menu.classList.remove("aperto");
        bottoneMenu.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- filtri galleria ---------- */
  var filtri = document.querySelectorAll(".filtro");
  if (filtri.length) {
    filtri.forEach(function (f) {
      f.addEventListener("click", function () {
        var scelta = f.dataset.filtro;
        filtri.forEach(function (x) {
          x.setAttribute("aria-pressed", x === f ? "true" : "false");
        });
        document.querySelectorAll(".opera").forEach(function (o) {
          o.hidden = !(scelta === "tutte" || o.dataset.sezione === scelta);
        });
        rinumera();
      });
    });
  }

  /* filtro iniziale preso dall'indirizzo, es. opere.html#scultura */
  if (filtri.length && location.hash) {
    var chiesto = decodeURIComponent(location.hash.slice(1));
    var bottone = document.querySelector('.filtro[data-filtro="' + chiesto + '"]');
    if (bottone) bottone.click();
  }

  /* ---------- ingranditore ---------- */
  var lente = document.querySelector(".lente");
  if (!lente) return;

  var imgLente = lente.querySelector("img");
  var didascalia = lente.querySelector("figcaption");
  var visibili = [];
  var indice = 0;

  /* Un'opera può avere più viste (data-viste). L'elenco dell'ingranditore le
     distende tutte: le frecce scorrono vista dopo vista, poi passano all'opera
     successiva. */
  function apribili() {
    var elenco = [];
    Array.prototype.forEach.call(
      document.querySelectorAll("[data-grande]"),
      function (el) {
        if (el.hidden || el.offsetParent === null) return;
        var viste = el.dataset.viste
          ? el.dataset.viste.split("|").filter(Boolean)
          : [el.dataset.grande];
        viste.forEach(function (src, k) {
          elenco.push({
            src: src,
            titolo: el.dataset.titolo || "",
            dati: el.dataset.dati || "",
            n: k + 1,
            totale: viste.length,
            origine: el
          });
        });
      }
    );
    return elenco;
  }

  function rinumera() { visibili = apribili(); }

  function mostra(i) {
    if (!visibili.length) return;
    indice = (i + visibili.length) % visibili.length;
    var v = visibili[indice];
    imgLente.src = v.src;
    imgLente.alt = v.titolo;
    didascalia.innerHTML = "";
    if (v.titolo) {
      var s = document.createElement("strong");
      s.textContent = v.titolo;
      didascalia.appendChild(s);
    }
    var riga = v.dati;
    if (v.totale > 1) {
      riga = (riga ? riga + " · " : "") + "vista " + v.n + " di " + v.totale;
    }
    if (riga) didascalia.appendChild(document.createTextNode(riga));
    // precarica le adiacenti
    [1, -1].forEach(function (off) {
      var a = visibili[(indice + off + visibili.length) % visibili.length];
      if (a) { var p = new Image(); p.src = a.src; }
    });
  }

  function apri(el) {
    rinumera();
    var i = -1;
    for (var k = 0; k < visibili.length; k++) {
      if (visibili[k].origine === el) { i = k; break; }
    }
    if (i < 0) {
      visibili = [{ src: el.dataset.grande, titolo: el.dataset.titolo || "",
                    dati: el.dataset.dati || "", n: 1, totale: 1, origine: el }];
      i = 0;
    }
    mostra(i);
    lente.classList.add("aperta");
    document.body.classList.add("bloccato");
    lente.querySelector(".chiudi").focus();
  }

  function chiudi() {
    lente.classList.remove("aperta");
    document.body.classList.remove("bloccato");
    imgLente.removeAttribute("src");
  }

  document.addEventListener("click", function (ev) {
    var el = ev.target.closest("[data-grande]");
    if (el) { ev.preventDefault(); apri(el); return; }
    if (ev.target.closest(".lente .chiudi")) return chiudi();
    if (ev.target.closest(".lente .prec")) return mostra(indice - 1);
    if (ev.target.closest(".lente .succ")) return mostra(indice + 1);
    if (ev.target === lente || ev.target.tagName === "FIGURE") {
      if (lente.classList.contains("aperta")) chiudi();
    }
  });

  document.addEventListener("keydown", function (ev) {
    if (!lente.classList.contains("aperta")) return;
    if (ev.key === "Escape") chiudi();
    else if (ev.key === "ArrowRight") mostra(indice + 1);
    else if (ev.key === "ArrowLeft") mostra(indice - 1);
  });

  /* scorrimento col dito */
  var x0 = null;
  lente.addEventListener("touchstart", function (e) { x0 = e.changedTouches[0].clientX; }, { passive: true });
  lente.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 55) mostra(indice + (dx < 0 ? 1 : -1));
    x0 = null;
  }, { passive: true });

  /* ---------- comparsa graduale ---------- */
  var daRivelare = document.querySelectorAll(".appare");
  if (daRivelare.length && "IntersectionObserver" in window) {
    var osservatore = new IntersectionObserver(function (voci) {
      voci.forEach(function (v) {
        if (v.isIntersecting) {
          v.target.classList.add("visibile");
          osservatore.unobserve(v.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    daRivelare.forEach(function (el) { osservatore.observe(el); });
  } else {
    daRivelare.forEach(function (el) { el.classList.add("visibile"); });
  }
})();
