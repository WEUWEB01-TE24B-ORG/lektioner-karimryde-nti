# Kapitel 6 – CSS Grid och kortmönster

Här är historiken över allt vi gjort i detta kapitel. Kapitlet introducerar CSS Grid – ett kraftfullt layoutverktyg för tvådimensionella layouter. Vi går från enkel 3-spalts-grid till avancerad explicit positionering och nästlade grids.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | burger-king | Byggt en produktsida med 3-kolumners grid-layout (`grid-template-columns: 1fr 1fr 1fr`). Använt hover-animationer med `transition` och `background-position`. Flexbox i sidhuvudet. |
| – | grid-layout | Demonstrationslektion med explicit 6×4-grid. Använt `grid-column` och `grid-row` med start/end-syntax för exakt elementplacering. Färgkodade boxar för visualisering. |
| – | raspberrypi | Byggt en artikel-sida med **nästlad grid** – yttre 3-kolumners grid och inre grid i varje kort för vertikal struktur. Modern kortdesign med hover-effekter. |

---

## Begrepp vi lärt oss

### CSS Grid
`display: grid`, `grid-template-columns`, `grid-template-rows`, `grid-column`, `grid-row`, `gap`, `fr`-enhet, nästlad grid (`display: grid` inuti grid-item), `repeat()`

### Övrigt CSS
`transition`, `background-position`, `linear-gradient`, `box-shadow`, `border-radius`, `:hover`, `display: flex`, `justify-content: space-between`, CSS-variabler, `100dvh`

---

## Exempel från lektionerna

### Enkel 3-kolumners grid (burger-king)
```css
.kolumner {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 30px;
}
.box {
    background: linear-gradient(to bottom, var(--beige) 50%, transparent 50%);
    background-size: 100% 200%;
    background-position: 0% 60%;
    border-radius: 15px;
    padding: 40px;
    transition: background-position 0.3s;
}
.box:hover {
    background-position: 0% 0%;  /* Fyll uppifrån */
}
```

### Explicit grid-positionering (grid-layout)
```css
.kontainer {
    height: 100dvh;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: auto 1fr auto auto;
    gap: 0px 5px;
}
.meny    { grid-column: 2 / 6; grid-row: 1; }
.artikel { grid-column: 2 / 3; grid-row: 2; }
img      { grid-column: 3 / 4; grid-row: 2; }
.sidfot  { grid-column: 2 / 6; grid-row: 3; }
```

### Nästlad grid för kortdesign (raspberrypi)
```css
.kolumner-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}
.kolumn {
    background-color: #fff;
    border-radius: 20px;
    display: grid;
    grid-template-rows: auto auto 1fr auto;  /* Inre grid */
}
.kolumn:hover {
    box-shadow: 0 5px 5px #AAA;
}
```

---

## Viktiga detaljer

- CSS Grid är ett **tvådimensionellt** layoutverktyg – till skillnad från flexbox som är endimensionellt.
- `fr` (fraction) fördelar tillgängligt utrymme proportionellt mellan grid-spår.
- `grid-column: 2 / 6` betyder "börja på linje 2, sluta på linje 6" – elementet spänner över 4 kolumner.
- Nästlad grid innebär att ett grid-item självt blir en grid-container.
- `100dvh` är "dynamic viewport height" och anpassar sig efter webbläsarens gränssnitt.
- `transition` skapar mjuka animationer när CSS-egenskaper ändras (t.ex. vid hover).
- CSS-reset med `box-sizing: border-box` används genomgående.
