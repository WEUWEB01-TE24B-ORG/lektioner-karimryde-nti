# Kapitel 1 – HTML-grunder och första CSS

Här är historiken över allt vi gjort i detta kapitel. Kapitlet introducerar HTML:s grundläggande byggstenar och progressivt mer avancerad CSS-styling. Vi går från enkel HTML-struktur till tabeller, Google Fonts och box-modellen.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | intro | Skapat vår allra första webbsida – en enkel HTML-sida med rubriker (`h1`, `h2`) och personlig information. Inget CSS än – bara webbläsarens standardstyling. |
| – | beatles | Stylat en låttext-sida med CSS-klasser (`.rad1`, `.rad2`). Använt bakgrundsbild, text-skugga, färger och typografi. Första mötet med CSS. |
| – | oppna-landskap | Importerat Google Fonts (`@import`), arbetat med RGBA-färger för genomskinlig bakgrund, box-modellen (`padding`, `border-radius`, `box-shadow`). |
| – | pippi | Fokuserat på semantisk HTML: `<strong>`, `<em>`, `<ul>`/`<li>`, `<img>` med `alt`-text, samt `lang="sv"` för svenskt innehåll. |
| – | veckomeny | Byggt en HTML-tabell (`<table>`, `<tr>`, `<th>`, `<td>`, `<caption>`) med matbilder. Stylat med `border-spacing`, `border-radius` och centrerat med `margin: auto`. |

---

## Begrepp vi lärt oss

### HTML
`<!DOCTYPE html>`, `<html lang="en">`, `<meta charset="UTF-8">`, `<meta name="viewport">`, `<title>`, `<h1>`–`<h6>`, `<p>`, `<br>`, `<strong>`, `<em>`, `<img src="" alt="">`, `<a href="">`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<tr>`, `<th>`, `<td>`, `<caption>`, `<span>`

### CSS
`color`, `background-color`, `background-image`, `background-size`, `font-family`, `font-size`, `font-weight`, `text-align`, `text-shadow`, `text-transform`, `margin`, `padding`, `width`, `border`, `border-radius`, `border-spacing`, `box-shadow`, `@import`, CSS-klasser (`.klassnamn`), RGBA-färger

---

## Exempel från lektionerna

### HTML5-grundskelett (intro)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Min första webbsida</title>
</head>
<body>
    <h1>Karim Ryde</h1>
    <h2>Follingbogatan 26</h2>
    <h2>Bromma</h2>
</body>
</html>
```

### CSS-klasser för olika textdelar (beatles)
```css
body {
    background-color: #c4a1a1;
    background-image: url(./bilder/bakgrund.jpg);
    background-size: cover;
}
h1 {
    color: #e06ae0;
    font-size: 100px;
    text-shadow: 2px 2px 10px black;
    text-align: center;
}
.rad1 { color: pink; }
.rad2 { color: palevioletred; }
```

### Google Fonts och box-modellen (oppna-landskap)
```css
@import url('https://fonts.googleapis.com/css2?family=Mea+Culpa&family=Nothing+You+Could+Do&display=swap');

h1 {
    font-family: "Nothing You Could Do", cursive;
    color: #FFF;
    text-shadow: 2px 2px 1px #111;
}
p {
    font-family: "Mea Culpa", cursive;
    background-color: #1e83e8aa;  /* RGBA – genomskinlig */
    width: 500px;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 2px 2px 1px #111;
}
```

### HTML-tabell med bilder (veckomeny)
```html
<table>
    <caption>Veckomeny v36 - NTI</caption>
    <tr>
        <th>Måndag</th>
        <th>Tisdag</th>
        <th>Onsdag</th>
    </tr>
    <tr>
        <td>Svamprisotto</td>
        <td>Kantarellpasta</td>
        <td>Blåbärspaj</td>
    </tr>
    <tr>
        <td><img src="./bilder/svamprisotto.jpg" alt="Svamprisotto"></td>
        <td><img src="./bilder/pasta.jpg" alt="Pasta"></td>
        <td><img src="./bilder/paj.jpg" alt="Paj"></td>
    </tr>
</table>
```

---

## Viktiga detaljer

- `<script>` placeras alltid sist i `<body>`, aldrig i `<head>`.
- `lang="en"` är standard; `lang="sv"` används när sidan är på svenska.
- CSS-klasser namnges på svenska i kebab-case (t.ex. `.rad1`, `.meny`).
- Alla filnamn skrivs i gemener med bindestreck, utan mellanslag.
- Bilder samlas i mappen `bilder/`.
- `@import` för Google Fonts placeras överst i CSS-filen.
