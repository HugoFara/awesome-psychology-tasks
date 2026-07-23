/* Client-side search over the generated index.
 *
 * No dependencies and no build step: the index is a flat array of small records
 * emitted by scripts/build_site.py. Scoring is deliberately simple — prefix and
 * substring matches on the title, then on the secondary fields — because the
 * corpus is a few thousand short records, not a document store.
 */
(function () {
  "use strict";

  var root = document.currentScript.dataset.base || "/";
  var form = document.getElementById("search-form");
  var input = document.getElementById("q");
  var status = document.getElementById("search-status");
  var list = document.getElementById("results");
  var filterBar = document.getElementById("filters");
  if (!form || !input || !list) return;

  var KINDS = { paradigm: "Paradigm", spec: "Specification", implementation: "Implementation" };
  var records = null;
  var kind = "all";
  var pending = null;

  function normalise(s) {
    return (s || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "");
  }

  // A paradigm and its specification are the catalog's own units; an implementation
  // is one instance of one. Searching "stroop" should surface the paradigm first,
  // then its spec, then the 30-odd tasks that implement it.
  var KIND_WEIGHT = { paradigm: 6, spec: 4, implementation: 0 };

  function score(rec, terms) {
    var title = rec._t;
    var blob = rec._b;
    var total = KIND_WEIGHT[rec.k] || 0;
    for (var i = 0; i < terms.length; i++) {
      var term = terms[i];
      if (title === term) total += 20;
      else if (title.startsWith(term)) total += 12;
      else if (title.indexOf(term) !== -1) total += 7;
      else if (blob.indexOf(term) !== -1) total += 2;
      else return 0;
    }
    return total;
  }

  function render(matches, query) {
    list.innerHTML = "";
    if (!query) {
      status.textContent = records.length.toLocaleString() + " records indexed. Type to search.";
      return;
    }
    if (!matches.length) {
      status.textContent = 'No match for "' + query + '".';
      return;
    }
    status.textContent =
      matches.length.toLocaleString() + (matches.length === 1 ? " match" : " matches");
    var frag = document.createDocumentFragment();
    matches.slice(0, 120).forEach(function (rec) {
      var li = document.createElement("li");
      var kindEl = document.createElement("p");
      kindEl.className = "result-kind";
      kindEl.textContent = KINDS[rec.k] || rec.k;
      var h = document.createElement("h3");
      var a = document.createElement("a");
      a.href = rec.k === "implementation" ? rec.u : root + rec.u;
      a.textContent = rec.t;
      if (rec.k === "implementation") {
        a.rel = "noopener";
        a.target = "_blank";
      }
      h.appendChild(a);
      li.appendChild(kindEl);
      li.appendChild(h);
      if (rec.s) {
        var p = document.createElement("p");
        p.className = "small muted";
        p.textContent = rec.s;
        li.appendChild(p);
      }
      var meta = document.createElement("p");
      meta.className = "meta";
      meta.textContent = [rec.p, rec.d].filter(Boolean).join(" · ");
      if (meta.textContent) li.appendChild(meta);
      frag.appendChild(li);
    });
    list.appendChild(frag);
    if (matches.length > 120) {
      var more = document.createElement("li");
      more.className = "small muted";
      more.textContent = "Showing the first 120 of " + matches.length.toLocaleString() + " matches.";
      list.appendChild(more);
    }
  }

  function run() {
    if (!records) return;
    var query = input.value.trim();
    var terms = normalise(query).split(/\s+/).filter(Boolean);
    var matches = [];
    if (terms.length) {
      for (var i = 0; i < records.length; i++) {
        var rec = records[i];
        if (kind !== "all" && rec.k !== kind) continue;
        var s = score(rec, terms);
        if (s > 0) matches.push([s, rec]);
      }
      matches.sort(function (a, b) {
        return b[0] - a[0] || a[1].t.localeCompare(b[1].t);
      });
      matches = matches.map(function (m) {
        return m[1];
      });
    }
    render(matches, query);
    var url = new URL(window.location.href);
    if (query) url.searchParams.set("q", query);
    else url.searchParams.delete("q");
    window.history.replaceState(null, "", url);
  }

  function schedule() {
    window.clearTimeout(pending);
    pending = window.setTimeout(run, 90);
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    run();
  });
  input.addEventListener("input", schedule);

  if (filterBar) {
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-kind]");
      if (!btn) return;
      kind = btn.dataset.kind;
      Array.prototype.forEach.call(filterBar.querySelectorAll("button"), function (b) {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      run();
    });
  }

  status.textContent = "Loading the index…";
  fetch(root + "search-index.json")
    .then(function (r) {
      if (!r.ok) throw new Error("index " + r.status);
      return r.json();
    })
    .then(function (data) {
      records = data;
      records.forEach(function (rec) {
        rec._t = normalise(rec.t);
        rec._b = normalise([rec.s, rec.p, rec.d, rec.a].filter(Boolean).join(" "));
      });
      input.disabled = false;
      var initial = new URL(window.location.href).searchParams.get("q");
      if (initial) input.value = initial;
      run();
      if (!initial) input.focus();
    })
    .catch(function (err) {
      status.textContent = "Could not load the search index (" + err.message + ").";
    });
})();
