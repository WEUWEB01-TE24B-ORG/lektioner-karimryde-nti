# Bedömning: Camen Sixten

**Total poäng: 19.5/20**

### 1. Grundläggande HTML & innehåll (5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **1p – Bildkomponent:** Använder `<figure>` och `<figcaption>` korrekt.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (5p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Snygg flex-lösning.
* **1p – Luft & rymd:** Bra avstånd.
* **1p – Designelement:** Följer designen väl.
* **1p – Stabilitet:** Layouten håller ihop bra.

### 3. Styling & detaljer (5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används korrekt.
* **1p – Typsnitt brödtext:** Sans-serif.
* **1p – Färger:** Korrekta färger.
* **1p – Aktiv sida:** Tydligt markerad med `.aktiv`.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (4.5p)
* **1p – Indentering & kommentarer:** Snygg och lättläst kod.
* **1p – Korrekta avstånd:** Inga `<br>`-lösningar.
* **1p – DRY:** Bra struktur.
* **0.5p – Logiska lösningar:** Du använder `margin-left: 150px` för att centrera menyn och bilden. Det fungerar eftersom du vet bredderna (700-400)/2, men det är bättre att använda `margin: 0 auto` på de inre elementen också. Då centreras de automatiskt oavsett bredd.
* **1p – Val av selektorer:** Bra och specifika selektorer.

---

**Sammanfattning:**

- **Styrkor:** Mycket välgjord inlämning! Du har full koll på struktur, semantik (figure/figcaption) och styling. Snyggt med flexbox på menyn och markering av aktiv sida.
- **Förbättringsområden:**
    - Det enda lilla att slipa på är att undvika hårdkodade marginaler för centrering (t.ex. `margin-left: 150px`). Prova `margin: 0 auto` på element med fast bredd (som din meny och figure) för att låta webbläsaren räkna ut centreringen åt dig.
