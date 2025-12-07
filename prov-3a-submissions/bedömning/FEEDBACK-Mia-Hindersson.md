# Bedömning: Mia Hindersson

**Total poäng: 14/20**

### 1. Grundläggande HTML & innehåll (4p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **0p – Bildkomponent:** Du använder `<div>` och `<h2>` för bilden. Instruktionen var att använda `<figure>` och `<figcaption>`.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Länkar finns. (Obs: Undvik mellanslag i filnamn).

### 2. Layout & utseende (3p)
* **0.5p – Kontainer:** Du har satt bredden till 800px, instruktionen sa 700px.
* **1p – Meny:** Ligger horisontellt.
* **1p – Luft & rymd:** Bra padding.
* **0.5p – Designelement:** Saknar skugga på kontainern.
* **0p – Stabilitet:** Du använder mycket "magic numbers" (t.ex. `margin-left: 252px`) för att placera saker. Det gör layouten instabil.

### 3. Styling & detaljer (3p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0p – Typsnitt brödtext:** Inte satt till sans-serif.
* **1p – Färger:** Korrekta färger.
* **0p – Aktiv sida:** Saknar markering för aktiv sida.
* **1p – Bildanpassning:** Bilden anpassas.

### 4. Kodkvalitet & struktur (4p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Ok.
* **0p – Logiska lösningar:** Stort avdrag för "magic numbers" för centrering. Använd `text-align: center` eller `margin: auto` istället.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** Du har kommit igång bra och fått ihop en fungerande sida.
- **Förbättringsområden:**
    - **Centrering:** Sluta gissa med `margin-left`! För att centrera text och bilder, använd `text-align: center` på föräldern (t.ex. `.kontainer` eller `.bild`). För att centrera block (som bilden om den har en bredd), använd `margin: 0 auto`.
    - **Semantik:** Använd `<figure>` och `<figcaption>` för bilder.
    - **Filnamn:** Undvik mellanslag i filnamn (`sida 1.html`).
