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

  function apribili() {
    return Array.prototype.filter.call(
      document.querySelectorAll("[data-grande]"),
      function (el) { return !el.hidden && el.offsetParent !== null; }
    );
  }

  function rinumera() { visibili = apribili(); }

  function mostra(i) {
    if (!visibili.length) return;
    indice = (i + visibili.length) % visibili.length;
    var el = visibili[indice];
    imgLente.src = el.dataset.grande;
    imgLente.alt = el.dataset.titolo || "";
    var t = el.dataset.titolo || "";
    var d = el.dataset.dati || "";
    didascalia.innerHTML = "";
    if (t) {
      var s = document.createElement("strong");
      s.textContent = t;
      didascalia.appendChild(s);
    }
    if (d) didascalia.appendChild(document.createTextNode(d));
    // precarica le adiacenti
    [1, -1].forEach(function (off) {
      var v = visibili[(indice + off + visibili.length) % visibili.length];
      if (v) { var p = new Image(); p.src = v.dataset.grande; }
    });
  }

  function apri(el) {
    rinumera();
    var i = visibili.indexOf(el);
    if (i < 0) { visibili = [el]; i = 0; }
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
