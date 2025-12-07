# Bedömning: Caspian Sandelius

**Total poäng: 18.5/20**

### 1. Grundläggande HTML & innehåll (5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **1p – Bildkomponent:** Använder `<figure>` och `<figcaption>` korrekt.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Länkar finns. (Obs: Undvik mellanslag i filnamn som `index 1.html`, använd bindestreck `index-1.html` istället).

### 2. Layout & utseende (4.5p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Centrerad och tydlig.
* **1p – Luft & rymd:** Bra padding.
* **0.5p – Designelement:** Saknar skugga (`box-shadow`) på kontainern som fanns i målbilden.
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (4.5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0.5p – Typsnitt brödtext:** Du använder Montserrat även för brödtexten. Instruktionen var att använda Montserrat för rubriker/meny och generell sans-serif (t.ex. Arial) för övrig text.
* **1p – Färger:** Korrekta färger.
* **1p – Aktiv sida:** Tydligt markerad.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (4.5p)
* **1p – Indentering & kommentarer:** Snygg kod.
* **1p – Korrekta avstånd:** Bra användning av padding/margin.
* **0.5p – DRY:** Du upprepar `font-family: Montserrat` på många ställen (`h1`, `.meny a`, `figcaption`, `p`). Det hade varit smidigare att sätta det på de element som ska ha det, och sätta en grundfont på `body`.
* **1p – Logiska lösningar:** Bra lösningar.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** Mycket bra inlämning! Du har följt instruktionerna väl och strukturen är solid. Snyggt med `<figure>` och `<figcaption>`.
- **Förbättringsområden:**
    - **Filnamn:** Undvik mellanslag i filnamn (`index 1.html`). Det kan skapa problem på webbservrar. Använd `index-1.html` eller `sida1.html`.
    - **Typsnitt:** Försök att skilja på rubriktypsnitt och brödtexttypsnitt för att skapa visuell hierarki (enligt instruktion).
    - **Skugga:** Glöm inte `box-shadow` på kontainern för att få det där lilla extra "lyftet" från bakgrunden.
