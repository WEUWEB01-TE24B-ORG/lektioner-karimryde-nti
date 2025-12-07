# Bedömning: Jack Carlsund

**Total poäng: 15/20**

### 1. Grundläggande HTML & innehåll (5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **1p – Bildkomponent:** Använder `<figure>` och `<figcaption>` korrekt.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (2.5p)
* **1p – Kontainer:** 700px och centrerad.
* **0.5p – Meny:** Du använder `margin-left: 140px` för att centrera menyn. Använd `text-align: center` istället.
* **0p – Luft & rymd:** Du använder `<br>`-taggar för att skapa avstånd i layouten. Detta är inte tillåtet enligt instruktionen. Använd `margin` och `padding` i CSS istället.
* **0.5p – Designelement:** `box-shadow` på `h1` har felaktig syntax och syns inte.
* **0.5p – Stabilitet:** Layouten är beroende av "magic numbers".

### 3. Styling & detaljer (4.5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0.5p – Typsnitt brödtext:** Du använder Montserrat även för brödtexten. Instruktionen var att använda Montserrat för rubriker/meny och generell sans-serif för övrig text.
* **1p – Färger:** Korrekta färger.
* **1p – Aktiv sida:** Tydligt markerad.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (3p)
* **1p – Indentering & kommentarer:** Godkänd.
* **0p – Korrekta avstånd:** Stort avdrag för användning av `<br>`.
* **1p – DRY:** Ok.
* **0p – Logiska lösningar:** `margin: center` är inte giltig CSS. Använd `margin: auto` för blockelement eller `text-align: center` för text/inline-element.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** Du har en bra grundstruktur och har använt `<figure>` och `<figcaption>` helt rätt.
- **Förbättringsområden:**
    - **VIKTIGT:** Sluta använda `<br>` för att göra mellanrum! Det är "bad practice". Använd CSS (`margin-top`, `margin-bottom`, `padding`) för att styra avståndet mellan element.
    - **Centrering:** Lär dig skillnaden på att centrera blockelement (som din kontainer) med `margin: auto` och text/länkar med `text-align: center`. Undvik att gissa med `margin-left`.
    - **CSS-syntax:** Kolla upp hur `box-shadow` fungerar.
