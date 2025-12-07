# Bedömning: Elias Wester

**Total poäng: 19.5/20**

### 1. Grundläggande HTML & innehåll (5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **1p – Bildkomponent:** Använder `<figure>` och `<figcaption>` korrekt.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (5p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Centrerad.
* **1p – Luft & rymd:** Bra padding.
* **1p – Designelement:** Följer designen väl.
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används korrekt.
* **1p – Typsnitt brödtext:** Sans-serif.
* **1p – Färger:** Korrekta färger.
* **1p – Aktiv sida:** Tydligt markerad.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (4.5p)
* **1p – Indentering & kommentarer:** Snygg kod.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Mycket bra, snyggt med en modern CSS-reset!
* **0.5p – Logiska lösningar:** `width: 69%` på `.navbar` är ett "magic number". Det fungerar här, men det är bättre att använda `text-align: center` på föräldern eller `display: flex; justify-content: center;` för att centrera menyn oavsett innehållets bredd.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** Mycket stark inlämning! Du har använt en modern CSS-reset vilket visar på ambition. Strukturen är klockren.
- **Förbättringsområden:**
    - Undvik "magic numbers" som `69%` för bredd. Försök hitta lösningar som fungerar oavsett exakt innehåll (t.ex. flexbox eller text-align).
