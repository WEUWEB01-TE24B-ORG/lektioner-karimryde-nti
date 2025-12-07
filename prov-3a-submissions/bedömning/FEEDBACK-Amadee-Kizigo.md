# Bedömning: Amadee Kizigo

**Total poäng: 11/20**

### 1. Grundläggande HTML & innehåll (2.5p)
* **1p – Grundstruktur:** Korrekt.
* **0.5p – Innehåll:** Saknar länk till Wikipedia i sidfoten.
* **0p – Bildkomponent:** Saknar `<figure>` och `<figcaption>`.
* **0p – Sidfot:** Saknas helt.
* **1p – Fem undersidor:** Länkar finns.

### 2. Layout & utseende (2.5p)
* **0p – Kontainer:** Saknar bredd (`width: px;` är ogiltigt) och centrering (`margin: auto` saknas).
* **1p – Meny:** Ligger horisontellt.
* **0.5p – Luft & rymd:** Finns viss luft, men layouten är trasig.
* **1p – Designelement:** Skuggor och färger finns.
* **0p – Stabilitet:** Layouten bygger på "magic numbers" (`margin-left: 400px`) vilket gör att den går sönder på mindre skärmar.

### 3. Styling & detaljer (3p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0p – Typsnitt brödtext:** Inte satt till sans-serif för brödtexten.
* **1p – Färger:** Korrekta färger på menyn.
* **0p – Aktiv sida:** Saknar markering.
* **1p – Bildanpassning:** `max-width: 100%` används korrekt.

### 4. Kodkvalitet & struktur (3p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Använder margin/padding.
* **0.5p – DRY:** Kan förbättras (sätt typsnitt på body istället för h1).
* **0p – Logiska lösningar:** Stort avdrag för `margin-left: 400px` för att försöka centrera innehåll. Använd en centrerad kontainer istället.
* **0.5p – Val av selektorer:** Generella selektorer.

---

**Sammanfattning:**

- **Styrkor:** Har kommit igång med CSS och använder `max-width` på bilder korrekt. Menyn ser okej ut.
- **Förbättringsområden:**
    - **Viktigt:** Fixa kontainern! Sätt `width: 700px;` och `margin: 0 auto;` på `.kontainer` för att centrera hela sidan snyggt.
    - Ta bort `margin-left: 400px` på rubriker och bilder. När kontainern är centrerad kommer innehållet hamna rätt automatiskt (eller med `text-align: center`).
    - Använd `<figure>` och `<figcaption>` för bilder.
    - Lägg till en sidfot med länk till Wikipedia.
