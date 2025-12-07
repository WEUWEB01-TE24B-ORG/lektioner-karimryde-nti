# Bedömning: Gustav Osterman

**Total poäng: 18/20**

### 1. Grundläggande HTML & innehåll (4.5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **0.5p – Bildkomponent:** Du använder `<figure>` och `<figcaption>`, men du har lagt `<figcaption>` *utanför* `<figure>`. Den ska ligga inuti.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (4p)
* **1p – Kontainer:** 700px och centrerad (du satte bredden på `body`, vilket fungerar men oftast sätter man den på `.kontainer`).
* **1p – Meny:** Centrerad.
* **0.5p – Luft & rymd:** Du saknar padding på själva kontainern, så innehållet kan hamna väldigt nära kanten.
* **0.5p – Designelement:** Saknar skugga på kontainern.
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **1p – Typsnitt brödtext:** Sans-serif.
* **1p – Färger:** Korrekta färger.
* **1p – Aktiv sida:** Tydligt markerad.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (4.5p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Ok.
* **0.5p – Logiska lösningar:** Att sätta `width: 700px` på `body` är lite ovanligt. Bättre att låta body vara 100% och sätta bredden på `.kontainer`.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** En bra och stabil inlämning. Du har löst det mesta korrekt.
- **Förbättringsområden:**
    - **HTML-struktur:** Flytta in `<figcaption>` i `<figure>`.
    - **Layout:** Sätt bredden på `.kontainer` istället för `body`, och lägg till lite `padding` i kontainern så texten får luft.
    - **Design:** Glöm inte `box-shadow`.
