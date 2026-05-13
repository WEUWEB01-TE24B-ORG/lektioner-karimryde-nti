# Kapitel 7 – Holy Grail-layout, responsiv design och `fr`-enheter

Här är historiken över allt vi gjort i detta kapitel. Kapitlet fördjupar CSS Grid med `grid-template-areas`, bygger den klassiska "Holy Grail"-layouten och introducerar responsiv design med media queries.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | fem-favoriter | Byggt en receptsida med navigering mellan 5 sidor. Använt `position: sticky` för meny, flexbox för nav-länkar, och lekfulla hover-effekter med `transform`. |
| – | holygrail | Implementerat den klassiska Holy Grail-layouten med CSS Grid och namngivna grid-areas (`sidhuvud`, `innehåll`, `sidebar`, `sidfot`). Blogg med artikel + sidebar. |
| – | neon-nudlar | Demonstrationsmall med alternativa grid-namn (`namn1`–`namn4`). Visar att grid-areas kan namnges godtyckligt. |
| – | responsiv-sida | Förberedelse för responsiv design – Holy Grail-layout som eleverna ska göra responsiv med media queries. |

---

## Begrepp vi lärt oss

### CSS Grid (avancerat)
`grid-template-areas`, `grid-area`, svenska områdesnamn (`sidhuvud`, `innehåll`, `sidebar`, `sidfot`, `sidopanel`), `fr`-enheter för proportionell bredd

### Övrigt CSS
`position: sticky`, `z-index`, `transform: translate()`, `transition`, `gap`, `linear-gradient`, `background-attachment: fixed`, `@media` queries (introduktion), `box-shadow`

---

## Exempel från lektionerna

### Holy Grail med grid-template-areas (holygrail)
```css
.kontainer {
    width: 1000px;
    margin: auto;
    display: grid;
    grid-template-columns: 3fr 1fr;
    gap: 20px;
    grid-template-areas:
        "sidhuvud sidhuvud"
        "innehåll sidebar"
        "sidfot   sidfot";
}
header  { grid-area: sidhuvud; }
main    { grid-area: innehåll; }
aside   { grid-area: sidebar; }
footer  { grid-area: sidfot; }
```

### Sticky navigation (fem-favoriter)
```css
nav {
    display: flex;
    gap: 10px;
    position: sticky;
    top: -20px;
    z-index: 1000;
}
nav a {
    background-color: #e69090;
    border-radius: 2px;
    padding: 5px;
    flex: 1;
    box-shadow: 2px 2px 0 #888;
    transition: all 0.2s ease-in-out;
}
nav a:hover {
    box-shadow: 0 0 0;
    background-color: #f3b7b7;
    transform: translate(2px, 2px);
}
```

### Alternativa grid-namn (neon-nudlar)
```css
.kontainer {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-areas:
        "namn1 namn1"
        "namn2 namn3"
        "namn4 namn4";
}
header  { grid-area: namn1; }
main    { grid-area: namn2; }
aside   { grid-area: namn3; }
footer  { grid-area: namn4; }
```

### Förberedelse för responsiv design (responsiv-sida)
```css
/* Detta är vad eleverna förväntas lägga till */
@media (max-width: 768px) {
    .kontainer {
        width: 100%;
        grid-template-columns: 1fr;
        grid-template-areas:
            "sidhuvud"
            "innehåll"
            "sidopanel"
            "sidfot";
    }
}
```

---

## Viktiga detaljer

- `grid-template-areas` är ett visuellt sätt att definiera layout – man "ritar" layouten med namn.
- Svenska områdesnamn (`sidhuvud`, `innehåll`, `sidebar`, `sidfot`) är konvention i kursen.
- `fr`-enheten fördelar utrymme proportionellt: `3fr 1fr` ger 75/25-fördelning.
- `position: sticky` gör att elementet stannar synligt vid scrollning.
- `transform: translate()` skapar rörelseeffekter utan att påverka layout-flödet.
- `@media` queries är nyckeln till responsiv design – de ändrar layout baserat på skärmstorlek.
- Holy Grail-layouten är en klassisk webbdesign: header, innehåll + sidebar, footer.
