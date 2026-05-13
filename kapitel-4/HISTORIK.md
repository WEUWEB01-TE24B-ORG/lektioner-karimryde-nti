# Kapitel 4 – Flersidig webbplats med gemensam navbar

Här är historiken över allt vi gjort i detta kapitel. Kapitlet fokuserar på att bygga en sammanhängande webbplats med flera sidor, en gemensam navigationsmeny och `.aktiv`-klass för att markera aktuell sida.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | favoriter | Byggt en webbplats med 5 sidor om favoritband. Varje sida har en gemensam `<div class="meny">` med länkar till alla sidor. Aktuell sida markeras med `class="aktiv"` – rent HTML-baserat, inget JavaScript. |

---

## Begrepp vi lärt oss

### HTML
Flersidig struktur (`sida1.html`–`sida5.html`), gemensam `<div class="meny">`, `class="aktiv"` på aktuell länk, `<figure>`/`<figcaption>`, `<div class="kontainer">`

### CSS
CSS-variabler (`:root`), `.meny a` – styling av meny-länkar, `.meny a.aktiv` – specifik styling för aktiv länk, `.meny a:hover` – hover-effekt, `display: inline-block`, `text-decoration: none`, `text-align: center`

---

## Exempel från lektionerna

### Gemensam navbar med .aktiv-klass (favoriter)
```html
<div class="meny">
    <a class="aktiv" href="sida1.html">ABBA</a>
    <a href="sida2.html">Manfred Mann</a>
    <a href="sida3.html">The Doors</a>
    <a href="sida4.html">The Beatles</a>
    <a href="sida5.html">Midnight Oil</a>
</div>
```

På sida2.html ändras enbart en rad:
```html
<div class="meny">
    <a href="sida1.html">ABBA</a>
    <a class="aktiv" href="sida2.html">Manfred Mann</a>
    <!-- ... -->
</div>
```

### CSS för meny och aktiv markering
```css
:root {
    --selective-yellow: #ffb703;
    --ut-orange: #fb8500;
}

.kontainer .meny a {
    text-decoration: none;
    background-color: var(--ut-orange);
    padding: 10px;
    width: 150px;
    display: inline-block;
    color: #fff;
}
.kontainer .meny a:hover {
    background-color: var(--selective-yellow);
}
.kontainer .meny a.aktiv {
    background-color: var(--selective-yellow);
}
```

### Figure med bildtext
```html
<figure>
    <img src="./bilder/ABBA_-_TopPop_1974_5.png.webp" alt="ABBA 1974">
    <figcaption>ABBA – medlemmarna från 1974</figcaption>
</figure>
```

---

## Viktiga detaljer

- `.aktiv` är en **egen klass**, inte CSS-pseudoklassen `:active`. Detta är en viktig konvention i kursen.
- Varje HTML-fil ansvarar själv för att markera sin länk som aktiv – inget JavaScript behövs.
- `display: inline-block` på meny-länkar gör att de beter sig som knappar men ligger på samma rad.
- CSS-variabler (`:root`) används för att enkelt hantera färgscheman.
- Gemensam CSS-fil för alla sidor – återanvändning är nyckeln till enhetlig design.
- `width: 900px; margin: auto;` på `.kontainer` centrerar innehållet på sidan.
