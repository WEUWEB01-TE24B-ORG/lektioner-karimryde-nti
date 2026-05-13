# Kapitel 3 – Div-boxar, CSS-klasser och flersidig navigering

Här är historiken över allt vi gjort i detta kapitel. Kapitlet är omfattande och introducerar `<div>`-boxar, CSS-klasser på body-elementet, flexbox, kortmönster (cards), CSS-variabler och flersidiga webbplatser.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | arbete | Byggt en serie på 6 HTML-sidor som tillsammans visar en dikt. Varje sida har unik bakgrund via `body.sida1`-klasser och navigering framåt/bakåt med `&laquo;`/`&raquo;`. |
| – | bildgalleri | Skapat ett NASA-bildgalleri med flexbox (`display: flex`). Använt `flex-direction: row-reverse` för att alternera bildplacering. Introducerat CSS-variabler (`:root`). |
| – | bloggen | Byggt en bloggsida med kortmönster (`.inlagg`), bildramar, box-shadow och lista-styling. Tränat på färgpaletter via CSS-variabler. |
| – | portfolio | En tom mall med `.kontainer` – grundstruktur för elevernas egna portfoliosidor. |
| – | scones | Skapat en receptsida med `<ul>` för ingredienser och `<ol>` för instruktioner. Använt `background-attachment: fixed` och bildramar. |
| – | visitkort | Designat ett digitalt visitkort med bakgrundsbild, `border-radius`, `box-shadow` och offset-text med padding. |

---

## Begrepp vi lärt oss

### HTML
`<div>`, `body` med klass (`<body class="sida1">`), `&laquo;`/`&raquo;` (HTML-entiteter), `<figure>`, `<figcaption>`, `<ul>`, `<ol>`, `<li>`, `<br>`, `<h1>`–`<h3>`

### CSS
`display: flex`, `flex-direction: row-reverse`, `:root { --variabel: värde; }`, `background-attachment: fixed`, `background-size: cover`, `box-shadow`, `border-radius`, `border`, `padding`, `margin: auto`, `width`, `list-style-type: square`, `text-decoration`, `@import`, `box-sizing: border-box`, CSS-reset

---

## Exempel från lektionerna

### Klassbaserad body för unik bakgrund per sida (arbete)
```css
body.sida1 { background-image: url(./bilder/pattern1.jpg); }
body.sida2 { background-image: url(./bilder/pattern2.jpg); }
body.sida3 { background-image: url(./bilder/pattern3.webp); }

div {
    width: 600px;
    padding: 50px;
    margin: 100px auto;
    background-color: #fff;
    border: 10px dotted #818181;
}
a {
    font-size: 30px;
    text-decoration: none;
    color: #F00;
}
```

### Flexbox för bildgalleri (bildgalleri)
```css
.box {
    display: flex;
    background-color: var(--gray);
    padding: 40px;
    margin-bottom: 40px;
}
.reverse {
    flex-direction: row-reverse;  /* Bild till höger istället */
}
img {
    width: 50%;
    margin-right: 30px;
}
```

### CSS-variabler och färgpalett (bildgalleri, bloggen)
```css
:root {
    --gray: #7E7D7D;
    --old-rose: #C47783;
    --van-dyke: #382E2A;
    --night: #0E100A;
}
body {
    background-color: var(--night);
    color: #fff;
}
```

### Blogg-kortmönster (bloggen)
```css
.inlagg {
    background-color: var(--burnt-sienna);
    padding: 40px;
    margin-bottom: 30px;
}
.inlagg img {
    width: 400px;
    border: 15px solid #fff;
    box-shadow: 2px 2px 10px #333;
    display: block;
    margin: auto;
}
```

### Recept med listor (scones)
```html
<h2>Ingredienser</h2>
<ul>
    <li>4 dl vetemjöl</li>
    <li>1 tsk salt</li>
</ul>
<h2>Gör så här</h2>
<ol>
    <li>Sätt ugnen på 225°C.</li>
    <li>Nyp ihop mjöl, salt och smör.</li>
</ol>
```

---

## Viktiga detaljer

- CSS-reset med `box-sizing: border-box` används genomgående från detta kapitel.
- `body` kan ha en klass för att ge olika sidor olika utseende med samma CSS-fil.
- `&laquo;` (vänsterpil) och `&raquo;` (högerpil) är HTML-entiteter för navigering.
- Flexbox (`display: flex`) är grunden för moderna layouter – här används det för bild/text-layouter.
- CSS-variabler (`--namn`) gör det enkelt att återanvända färger och byta färgschema.
- `background-attachment: fixed` låser bakgrundsbilden vid scrollning (parallax-effekt).
