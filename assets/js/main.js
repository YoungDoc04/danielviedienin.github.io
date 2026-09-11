(function () {
  "use strict";

  /* ---- Mobile burger menu ---- */
  var burger = document.querySelector(".burger");
  var panel = document.querySelector(".site-header__right");

  if (burger && panel) {
    burger.addEventListener("click", function () {
      var isOpen = panel.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    panel.addEventListener("click", function (event) {
      if (event.target.tagName === "A") {
        panel.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && panel.classList.contains("is-open")) {
        panel.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
        burger.focus();
      }
    });
  }

  /* ---- Language switcher ----
     Swaps the leading /en/ /ua/ /ru/ segment of the current path for
     the chosen language and keeps the remainder of the path intact.
     Individual blog posts/notes are not language-prefixed (see
     README), so on those pages — or on any path with no recognised
     prefix — this falls back to that language's homepage. */
  var LANG_PREFIX = /^\/(en|ua|ru)(\/|$)/;

  document.querySelectorAll("[data-lang-switch]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var lang = btn.getAttribute("data-lang-switch");
      var path = window.location.pathname;
      var match = path.match(LANG_PREFIX);
      var target;

      if (match) {
        target = path.replace(LANG_PREFIX, "/" + lang + "/");
      } else {
        target = "/" + lang + "/";
      }

      window.location.href = target + window.location.search + window.location.hash;
    });
  });
})();
