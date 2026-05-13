# Kapitel 2 – Bilder, figurer och layoutövningar

Här är historiken över allt vi gjort i detta kapitel. Kapitlet fokuserar på bildhantering i CSS, HTML5-figurer (`<figure>`/`<figcaption>`) och layout med bakgrundsbilder.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | fiji-reklamsida | Skapat en reklamsida för Fiji med stor bakgrundsbild (`background-size: cover`), text-skuggor, `text-transform: uppercase`, och en CTA-knapp (`<a>` stylad som knapp med padding, border-radius). |
| – | portrattsida | Tom övningsmall – eleverna ska själva bygga en liknande sida med `<figure>` och `<figcaption>`. |

---

## Begrepp vi lärt oss

### HTML
`<figure>`, `<figcaption>`, `<h1>`, `<h2>`, `<p>`, `<a>`, `<img>`

### CSS
`background-image`, `background-size: cover`, `background-position`, `text-transform: uppercase`, `text-shadow`, `text-decoration: none`, `border-radius`, `border`, `padding`, `margin`, `font-family: sans-serif`

---

## Exempel från lektionerna

### Bakgrundsbild med positionering (fiji-reklamsida)
```css
body {
    background-image: url(./bilder/fiji.jpg);
    background-size: cover;
    background-position: 0 -300px;  /* Flytta upp bilden */
}
h1 {
    font-family: sans-serif;
    color: #5a2d7c;
    font-size: 50px;
    text-transform: uppercase;
    text-shadow: 2px 2px 1px #e1f4f7;
    margin-top: 100px;
    margin-left: 100px;
}
```

### Knappdesign med `<a>`-tagg (fiji-reklamsida)
```css
a {
    color: #fff;
    text-transform: uppercase;
    text-decoration: none;
    background-color: darkorchid;
    padding: 10px 50px 10px 50px;
    border-radius: 5px;
    border: 1px solid #fff;
}
```

### Figure och figcaption (portrattsida – mall)
```html
<figure>
    <img src="./bilder/portratt.jpg" alt="Porträtt">
    <figcaption>Bildtext här</figcaption>
</figure>
```

---

## Viktiga detaljer

- `<figure>` och `<figcaption>` är HTML5-element för semantisk bildhantering.
- `background-position` med negativa värden kan användas för att beskära bakgrundsbilder kreativt.
- En `<a>`-tagg kan stylas som en knapp med `padding`, `border-radius` och `background-color`.
- `text-shadow` förbättrar läsbarheten av text över bilder.
- Bilder från Unsplash används som kostnadsfria högkvalitativa bilder.
