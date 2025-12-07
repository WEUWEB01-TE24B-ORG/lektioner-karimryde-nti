# Bedömning: Cengiz Deniz

**Total poäng: 18/20**

### 1. Grundläggande HTML & innehåll (5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **1p – Bildkomponent:** Använder `<figure>` och `<figcaption>` korrekt.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Länkar finns. (Obs: Undvik mellanslag i filnamn).

### 2. Layout & utseende (5p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Centrerad.
* **1p – Luft & rymd:** Bra padding.
* **1p – Designelement:** Följer designen väl.
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (3.5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0.5p – Typsnitt brödtext:** Du använder Montserrat för det mesta. Instruktionen var att använda Montserrat för rubriker/meny och generell sans-serif för övrig text.
* **1p – Färger:** Korrekta färger.
* **0p – Aktiv sida:** Saknar markering för aktiv sida i menyn.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (4.5p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Bra struktur.
* **0.5p – Logiska lösningar:** `display: flexbox;` är inte giltig CSS. Det ska vara `display: flex;` eller `display: inline-flex;`. Nu fungerar det ändå för att länkarna är inline-element och du har `text-align: center`, men koden är felaktig.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** Bra jobbat! Du har en stabil grund och har löst de flesta uppgifterna galant. Snyggt med `<figure>` och `<figcaption>`.
- **Förbättringsområden:**
    - **Filplacering:** Du lade dina filer i `dump`-mappen. Se till att lägga dem direkt i roten nästa gång så de är lätta att hitta.
    - **CSS-syntax:** `display: flexbox` finns inte. Läs på om Flexbox (det heter `display: flex`).
    - **Aktiv sida:** Glöm inte att markera vilken sida användaren är på i menyn.
    - **Filnamn:** Undvik mellanslag i filnamn (`index 1.html`).
