# Bedömning: Viktor Karlsen

**Total poäng: 16/20**

### 1. Grundläggande HTML & innehåll (4.5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **0.5p – Bildkomponent:** Du använder `<figure>` men inuti använder du `<h2>` istället för `<figcaption>`.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (4.5p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Centrerad.
* **1p – Luft & rymd:** Bra padding.
* **0.5p – Designelement:** Saknar skugga på kontainern.
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (2p)
* **0p – Typsnitt rubrik/meny:** Du importerar Montserrat men använder det aldrig i din CSS. Du måste skriva `font-family: 'Montserrat', sans-serif;` på de element som ska ha det (t.ex. `h1`, `.meny a`).
* **1p – Typsnitt brödtext:** Sans-serif.
* **1p – Färger:** Korrekta färger.
* **0p – Aktiv sida:** Du har lagt in en tom `<div class="aktiv"></div>` i menyn. För att markera aktiv sida ska du lägga klassen `aktiv` på själva `<a>`-länken (t.ex. `<a href="..." class="aktiv">`) och sedan styla den i CSS.
* **0p – Bildanpassning:** Du saknar `max-width: 100%` på bilden, vilket gör att den kan bli för bred för behållaren.

### 4. Kodkvalitet & struktur (5p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Ok.
* **1p – Logiska lösningar:** Bra lösningar.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** Bra grundstruktur och layout.
- **Förbättringsområden:**
    - **Typsnitt:** Glöm inte att faktiskt *använda* typsnittet du importerar.
    - **Semantik:** Använd `<figcaption>` inuti `<figure>`.
    - **Aktiv sida:** Läs på om hur man lägger klasser på länkar för att styla dem olika.
    - **Bild:** Sätt alltid `max-width: 100%` på bilder i responsiv design.
