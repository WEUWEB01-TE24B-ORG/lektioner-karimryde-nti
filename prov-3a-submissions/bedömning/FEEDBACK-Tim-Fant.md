# Bedömning: Tim Fant

**Total poäng: 11/20**

### 1. Grundläggande HTML & innehåll (3.5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **0p – Bildkomponent:** Saknar `<figure>` och `<figcaption>`.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **0.5p – Fem undersidor:** Du har stavfel i länken till statyn (`ststyn.html` istället för `statyn.html`).

### 2. Layout & utseende (2.5p)
* **0.5p – Kontainer:** Du använder `margin-left: 300px` för att centrera. Det fungerar bara på din skärm. Använd `margin: auto` för att centrera automatiskt.
* **0p – Meny:** Dina CSS-selektorer för menyn är felaktiga, så länkarna ser inte ut som de ska.
* **1p – Luft & rymd:** Bra padding.
* **0.5p – Designelement:** `box-shadow: solid ...` är felaktig syntax. Ta bort `solid`.
* **0.5p – Stabilitet:** Layouten är beroende av "magic numbers".

### 3. Styling & detaljer (2p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0p – Typsnitt brödtext:** Inte satt till sans-serif.
* **0p – Färger:** Syns inte pga felaktiga selektorer.
* **0p – Aktiv sida:** Fungerar ej pga felaktiga selektorer.
* **1p – Bildanpassning:** `width: 100%` används korrekt.

### 4. Kodkvalitet & struktur (3p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Ok.
* **0p – Logiska lösningar:** Stort avdrag för `margin-left` för centrering och felaktig CSS-syntax.
* **0p – Val av selektorer:** Du skriver `.kontainer .box .sidhuvud a` i CSS, vilket betyder "en länk inuti ett element med klassen sidhuvud". Men i HTML har du satt klassen *på* länken (`<a class="sidhuvud">`). Rätt selektor är `.kontainer .box a.sidhuvud` eller bara `.kontainer .box a`.

---

**Sammanfattning:**

- **Styrkor:** Du har fått ihop grunden och bildanpassningen fungerar bra.
- **Förbättringsområden:**
    - **CSS-selektorer:** Se över hur du väljer element i CSS. Om en `<a>`-tagg har klassen `sidhuvud`, skriver du `a.sidhuvud` i CSS, inte `.sidhuvud a`.
    - **Centrering:** Använd alltid `margin: 0 auto;` för att centrera en kontainer med fast bredd. Använd aldrig `margin-left` med ett stort pixelvärde för detta.
    - **HTML-struktur:** Använd `<figure>` och `<figcaption>` för bilder.
    - **Stavning:** Kolla dina filnamn och länkar noga (`ststyn.html`).
