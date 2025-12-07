# Bedömning: Brian Nwaijah

**Total poäng: 15.5/20**

### 1. Grundläggande HTML & innehåll (3.5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **0p – Bildkomponent:** Saknar `<figure>` och `<figcaption>`. Använder `<div>` och `<footer>` felaktigt här.
* **0.5p – Sidfot:** Länk finns på startsidan, men saknas på undersidor. `<footer>` används felaktigt till bildtexten.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (5p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Ligger horisontellt.
* **1p – Luft & rymd:** Bra padding.
* **1p – Designelement:** Stämmer väl överens med målbilden.
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (3.5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **1p – Typsnitt brödtext:** Sans-serif.
* **1p – Färger:** Korrekta färger på menyn.
* **0p – Aktiv sida:** Saknar markering för aktiv sida.
* **0.5p – Bildanpassning:** Bilden har ram men saknar `max-width` för responsivitet/säkerhet.

### 4. Kodkvalitet & struktur (3.5p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Använder padding/margin.
* **1p – DRY:** Bra.
* **0p – Logiska lösningar:** Använder "magic numbers" (`padding-left: 160px`, `padding-left: 200px`) för att centrera text istället för `text-align: center`.
* **0.5p – Val av selektorer:** Använder generell `a`-selektor som påverkar alla länkar, även sidfotslänken.

---

**Sammanfattning:**

- **Styrkor:** Grundstrukturen är på plats och designen efterliknar målbilden väl med färger och skuggor. Menyn är tydlig och fungerar.
- **Förbättringsområden:**
    - Använd `<figure>` och `<figcaption>` för bilder och bildtexter istället för `<div>` och `<footer>`. `<footer>` ska användas för sidfoten längst ner på sidan.
    - Undvik "magic numbers" (t.ex. `padding-left: 160px`) för att centrera text. Använd `text-align: center` istället för en mer robust lösning.
    - Markera den aktiva sidan i menyn (t.ex. med en klass `.active`) för att visa användaren var de befinner sig.
    - Se till att Wikipedia-länken finns med på alla undersidor.
