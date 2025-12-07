# Bedömning: Lazar Tasic

**Total poäng: 15.5/20**

### 1. Grundläggande HTML & innehåll (5p)
* **1p – Grundstruktur:** Korrekt.
* **1p – Innehåll:** Allt finns med.
* **1p – Bildkomponent:** Använder `<figure>` och `<figcaption>` korrekt.
* **1p – Sidfot:** Länk till Wikipedia finns.
* **1p – Fem undersidor:** Korrekt länkade.

### 2. Layout & utseende (4p)
* **1p – Kontainer:** 700px och centrerad.
* **1p – Meny:** Centrerad.
* **1p – Luft & rymd:** Bra padding.
* **0p – Designelement:** Du har flera syntaxfel i din CSS som gör att designen inte syns som den ska (se nedan).
* **1p – Stabilitet:** Layouten håller ihop.

### 3. Styling & detaljer (2.5p)
* **1p – Typsnitt rubrik/meny:** Montserrat används.
* **0.5p – Typsnitt brödtext:** Du använder Montserrat även för brödtexten. Instruktionen var att använda Montserrat för rubriker/meny och generell sans-serif för övrig text.
* **0p – Färger:** Syns inte pga syntaxfel.
* **0p – Aktiv sida:** Du har lagt till klassen `.aktiv` i HTML men saknar CSS-kod för den.
* **1p – Bildanpassning:** Bilden anpassas efter behållaren.

### 4. Kodkvalitet & struktur (4p)
* **1p – Indentering & kommentarer:** Godkänd.
* **1p – Korrekta avstånd:** Bra.
* **1p – DRY:** Ok.
* **0p – Logiska lösningar:** Stort avdrag för syntaxfel i CSS.
* **1p – Val av selektorer:** Bra.

---

**Sammanfattning:**

- **Styrkor:** HTML-strukturen är mycket bra och du har använt `<figure>` och `<figcaption>` helt rätt.
- **Förbättringsområden:**
    - **CSS-syntax:** Du har blandat ihop egenskap och värde på flera ställen.
        - `background: color #666;` -> Ska vara `background-color: #666;`
        - `font: size 40px;` -> Ska vara `font-size: 40px;`
        - `border: radius 5px;` -> Ska vara `border-radius: 5px;`
    - **Aktiv sida:** Glöm inte att styla `.aktiv` i CSS så att den syns.
