# WEUWEB01 – Webbutveckling 1

Lektionsarkiv för gymnasiekursen Webbutveckling 1 (TE23A). Detta repo innehåller all kod som producerats under kursens gång – från första HTML-sidan till interaktiv JavaScript.

## Kursöversikt

Kursen introducerar webbutveckling genom praktiskt arbete med HTML, CSS och grundläggande JavaScript. Varje kapitel bygger på det föregående med extrem repetition – varje nytt koncept övas flera gånger i olika sammanhang.

| Kapitel | Tema | Antal lektioner |
|---------|------|-----------------|
| 1 | HTML-grunder och första CSS | 5 |
| 2 | Bilder, figurer och layoutövningar | 2 |
| 3 | Div-boxar, CSS-klasser och flersidig navigering | 6 |
| 4 | Flersidig webbplats med gemensam navbar | 1 (5 sidor) |
| 6 | CSS Grid och kortmönster | 3 |
| 7 | Holy Grail-layout, responsiv design och `fr`-enheter | 4 |
| 8 | JavaScript, DOM-manipulation och händelser | 6 |

> Kapitel 5 (semantisk HTML) är inte representerat i detta arkiv.

---

## Kapitel 1 – HTML-grunder och första CSS

**Syfte:** Förstå webbens grundsten – HTML – och hur CSS används för att styla innehåll.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **HTML-element** | Byggstenarna i en webbsida: `<h1>`, `<p>`, `<img>`, `<a>`, `<table>`, `<ul>`, `<li>` |
| **HTML5-skelett** | `<!DOCTYPE html>`, `<meta charset="UTF-8">`, `<meta name="viewport">` – grunden varje sida behöver |
| **CSS-selektorer** | `h1`, `.klass`, `body` – hur man väljer vad som ska stylas |
| **Box-modellen** | `margin`, `padding`, `border`, `width` – hur utrymme runt element fungerar |
| **Google Fonts** | Importera externa typsnitt med `@import` |
| **RGBA-färger** | Färger med genomskinlighet, t.ex. `#1e83e8aa` |

### Exempel: Box-modellen

```css
p {
    background-color: #1e83e8aa;  /* RGBA – sista "aa" är genomskinlighet */
    width: 500px;
    padding: 20px;       /* luft inuti */
    border-radius: 10px; /* rundade hörn */
    box-shadow: 2px 2px 1px #111;  /* skugga bakom */
}
```

**Koppling till centralt innehåll:**
- Märkspråk och deras syntax/semantik (HTML-standarder)
- Teckenkodning (`<meta charset="UTF-8">`)
- Riktlinjer för god praxis (korrekt HTML5-struktur)

---

## Kapitel 2 – Bilder, figurer och layoutövningar

**Syfte:** Hantera bilder korrekt i HTML och CSS samt förstå semantiska bildelement.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **`<figure>` / `<figcaption>`** | Semantisk HTML för bilder med bildtext |
| **`background-image`** | CSS-egenskap för bakgrundsbilder |
| **`background-size: cover`** | Täcker hela elementet med bilden |
| **`background-position`** | Styr vilken del av bilden som visas |
| **CTA-knapp** | Call-to-action – en länk stylad som knapp |

### Exempel: Bakgrundsbild som designelement

```css
body {
    background-image: url(./bilder/fiji.jpg);
    background-size: cover;
    background-position: 0 -300px;  /* Flytta fokus uppåt */
}
a {
    text-decoration: none;
    background-color: darkorchid;
    padding: 10px 50px;
    border-radius: 5px;
    color: #fff;
}
```

**Koppling till centralt innehåll:**
- Bilder och media med alternativa format, optimering och tillgänglighet
- `<figure>` och `<figcaption>` ger semantisk struktur och tillgänglighet

---

## Kapitel 3 – Div-boxar, CSS-klasser och flersidig navigering

**Syfte:** Strukturera innehåll med `<div>`-behållare, använda flexbox för layout, och skapa sammanhängande flersidiga webbplatser.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **`<div>`** | Generisk behållare för att gruppera och styla innehåll |
| **Flexbox** | `display: flex` – endimensionell layout för rader/kolumner |
| **CSS-variabler** | `:root { --färg: #värde; }` – återanvändbara värden |
| **CSS-reset** | Nollställer webbläsarens standardmarginaler för konsekvent design |
| **HTML-entiteter** | `&laquo;` (») och `&raquo;` («) för specialtecken |
| **`background-attachment: fixed`** | Låser bakgrundsbilden vid scrollning (parallax) |

### Exempel: CSS-variabler och flexbox

```css
:root {
    --gray: #7E7D7D;
    --night: #0E100A;
}
body {
    background-color: var(--night);
}
.box {
    display: flex;
    padding: 40px;
}
.reverse {
    flex-direction: row-reverse;  /* Bild till höger */
}
```

### Exempel: Klassbaserad body för olika sidor

```css
body.sida1 { background-image: url(./bilder/pattern1.jpg); }
body.sida2 { background-image: url(./bilder/pattern2.jpg); }
/* Samma CSS-fil – olika bakgrund via body-klass */
```

**Koppling till centralt innehåll:**
- Märkspråk och deras inbördes roller (HTML för struktur, CSS för presentation)
- Interoperabilitet – samma CSS fungerar på alla webbläsare
- Dokumentation (README i varje mapp)

---

## Kapitel 4 – Flersidig webbplats med gemensam navbar

**Syfte:** Förstå hur en komplett webbplats med flera sidor fungerar – gemensam navigering och aktiv markering.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **`.aktiv`-klass** | Markerar aktuell sida i navigeringen (ej CSS-pseudoklassen `:active`) |
| **Gemensam navbar** | Samma `<div class="meny">` på alla sidor |
| **`display: inline-block`** | Gör element till block men håller dem på samma rad |
| **`text-decoration: none`** | Tar bort understrykning på länkar |

### Exempel: Aktiv markering utan JavaScript

```html
<!-- På sida2.html -->
<div class="meny">
    <a href="sida1.html">ABBA</a>
    <a class="aktiv" href="sida2.html">Manfred Mann</a>  <!-- Bara denna markerad -->
    <a href="sida3.html">The Doors</a>
</div>
```
```css
.meny a.aktiv {
    background-color: var(--selective-yellow);  /* Gul markering */
}
```

**Koppling till centralt innehåll:**
- Publikation av webbplatser (flersidig struktur utan CMS)
- Processen för webbutvecklingsprojekt (planering → struktur → kodning → testning)
- Interoperabilitet – fungerar utan JavaScript, i alla webbläsare

---

## Kapitel 6 – CSS Grid och kortmönster

**Syfte:** Introducera CSS Grid – ett tvådimensionellt layoutverktyg som ersätter äldre tekniker. Bygga moderna kortlayouter.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **CSS Grid** | `display: grid` – tvådimensionell layout med rader och kolumner |
| **`fr`-enhet** | "Fraction" – fördelar tillgängligt utrymme proportionellt |
| **`grid-template-columns`** | Definierar antal och storlek på kolumner |
| **`grid-column` / `grid-row`** | Explicit placering med start/end-linjer |
| **Nästlad grid** | Ett grid-item som självt är en grid-container |
| **`transition`** | Mjuk övergång mellan CSS-tillstånd (t.ex. hover) |
| **`100dvh`** | Dynamic viewport height – full skärmhöjd |

### Exempel: 3-kolumners grid med hover-effekt

```css
.kolumner {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;  /* Tre lika breda kolumner */
    gap: 30px;
}
.box {
    background: linear-gradient(to bottom, beige 50%, transparent 50%);
    background-size: 100% 200%;
    transition: background-position 0.3s;
}
.box:hover {
    background-position: 0% 0%;  /* Fyller kortet uppifrån */
}
```

### Exempel: Explicit grid-positionering

```css
.kontainer {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: auto 1fr auto auto;
}
.meny    { grid-column: 2 / 6; grid-row: 1; }  /* Spänner 4 kolumner */
.artikel { grid-column: 2 / 3; grid-row: 2; }
```

**Koppling till centralt innehåll:**
- Modern layout-teknik som ersätter tabellbaserade layouter
- Interoperabilitet – CSS Grid stöds av alla moderna webbläsare
- Kvalitetssäkring – grid-baserad layout är förutsägbar och testbar

---

## Kapitel 7 – Holy Grail-layout, responsiv design och `fr`-enheter

**Syfte:** Använda namngivna grid-areas för komplexa layouter, förstå "Holy Grail"-mönstret och introducera responsiv design.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **`grid-template-areas`** | Visuellt sätt att "rita" layouten med namn |
| **Holy Grail-layout** | Klassiskt webbmönster: header, innehåll + sidebar, footer |
| **`position: sticky`** | Element stannar synligt vid scrollning |
| **`transform: translate()`** | Flyttar element utan att påverka layout-flödet |
| **`@media` queries** | Villkorsstyr CSS baserat på skärmstorlek |
| **Responsiv design** | Layout som anpassar sig efter enhetens skärm |

### Exempel: Holy Grail med grid-template-areas

```css
.kontainer {
    display: grid;
    grid-template-columns: 3fr 1fr;
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

### Exempel: Responsiv design med media query

```css
@media (max-width: 768px) {
    .kontainer {
        grid-template-columns: 1fr;
        grid-template-areas:
            "sidhuvud"
            "innehåll"
            "sidebar"
            "sidfot";
    }
}
```

**Koppling till centralt innehåll:**
- Applikationer som fungerar oberoende av användaragent (responsiv design)
- Tillgänglighet för användare med olika enheter
- Testning på olika skärmstorlekar
- Standarder – `@media` queries är en W3C-standard

---

## Kapitel 8 – JavaScript, DOM-manipulation och händelser

**Syfte:** Introducera programmering i webbläsaren – hur JavaScript kan läsa och ändra HTML/CSS efter att sidan laddats.

### Viktiga begrepp

| Begrepp | Förklaring |
|---------|------------|
| **`let`** | Deklarerar en variabel (föränderlig) |
| **`function()`** | Namngiven funktion som kan anropas |
| **`onclick`** | HTML-attribut som kopplar en funktion till ett klick |
| **DOM** | Document Object Model – sidans struktur som JavaScript kan nå |
| **`document.querySelector()`** | Hittar ett HTML-element med CSS-selektor |
| **`.textContent`** | Läser/skriver textinnehåll i ett element |
| **`.value`** | Läser/skriver värdet i ett input-fält |
| **`.style`** | Ändrar CSS-egenskaper direkt via JavaScript |
| **`Number()`** | Konverterar text till tal |
| **`prompt()`** | Visar en inmatningsruta för användaren |
| **`alert()`** | Visar en popup-ruta med text |

### Exempel: Miniräknare med färgkodning

```html
<input class="tal1" placeholder="Första talet">
<input class="tal2" placeholder="Andra talet">
<button onclick="addera()">+</button>
<p class="resultat">Resultatet visas här</p>
```
```javascript
function addera() {
    let tal1 = document.querySelector(".tal1").value;
    let tal2 = document.querySelector(".tal2").value;
    let summa = Number(tal1) + Number(tal2);
    document.querySelector(".resultat").textContent = "Summan är = " + summa;

    if (summa == 0) {
        document.querySelector(".resultat").style.backgroundColor = "yellow";
    } else if (summa > 0) {
        document.querySelector(".resultat").style.backgroundColor = "green";
    } else {
        document.querySelector(".resultat").style.backgroundColor = "red";
    }
}
```

### Exempel: Klick-händelse direkt i HTML

```html
<h1 onclick="kaboom()">Klicka här!</h1>
<script>
function kaboom() {
    document.body.style.backgroundColor = "red";
}
</script>
```

**Koppling till centralt innehåll:**
- ECMAScript och dokumentobjektsmodellen (DOM)
- Samspelet mellan klient och server (JavaScript körs på klienten)
- Kvalitetssäkring – testning av funktionalitet
- Säkerhet – `prompt()` och `alert()` är säkra, kontrollerade inmatningssätt

---

## Teknisk orientering om webbens protokoll och samspel

Under kursens gång har vi praktiskt erfarenhet av:

- **HTTP/HTTPS:** Alla sidor öppnas via `http://` eller `file://`-protokollet. Bildlänkar och externa resurser (Google Fonts, Unsplash-bilder) hämtas via HTTPS.
- **Klient-server-modellen:** Webbläsaren (klienten) begär HTML-filer, CSS-filer, bilder och JavaScript-filer – servern svarar med dessa resurser.
- **Adresser (URL:er):** Absoluta och relativa sökvägar används genomgående: `./bilder/foto.jpg`, `sida2.html`, `https://fonts.googleapis.com/...`.
- **Säkerhet:** Externa resurser från betrodda källor (Google Fonts, Wikipedia, Unsplash). `alt`-texter på bilder för tillgänglighet.

---

## Processen för webbutvecklingsprojekt

Varje lektion följer en återkommande arbetsgång:

1. **Målsättning:** Läraren presenterar dagens koncept
2. **Specifikation:** Kodningsmallen gås igenom på tavlan
3. **Struktur och design:** HTML-skelett och CSS planeras
4. **Kodning:** Eleverna skriver och testar koden
5. **Optimering:** Bilder komprimeras, CSS återanvänds
6. **Testning:** Sidan öppnas i webbläsaren, problem åtgärdas
7. **Dokumentation:** README.md och HISTORIK.md sammanfattar

---

## Konventioner i kursen

### HTML
- `<!DOCTYPE html>` och `lang="en"` (eller `lang="sv"` för svenska sidor)
- `<meta charset="UTF-8">` för korrekt teckenkodning
- `<meta name="viewport">` för responsivt beteende
- `<script>` placeras **alltid sist i `<body>`**
- Aktiv nav-länk markeras med `class="aktiv"`

### CSS
- CSS-reset från kapitel 3 och framåt:
  ```css
  html { box-sizing: border-box; }
  *, *:before, *:after { box-sizing: inherit; }
  body, h1, h2, h3, h4, h5, h6, p, ul { margin: 0; padding: 0; }
  img { width: 100%; }
  ```
- Centrering: `.kontainer { width: Xpx; margin: auto; }`
- Grid-areas på svenska: `sidhuvud`, `innehåll`, `sidebar`, `sidfot`
- Klasser i kebab-case: `.meny`, `.inlagg`, `.rutnat`, `.aktiv`

### JavaScript (kapitel 8)
- Endast `let` (inte `const` eller `var`)
- `onclick`-attribut i HTML, inte `addEventListener`
- Namngivna funktioner: `function addera()`
- Inga loopar, arrayer, objekt

### Filnamn
- Gemener, kebab-case: `oppna-landskap`, `index.html`, `style.css`
- Bilder i `bilder/`-mappen
- Flersidiga sidor: `sida1.html`, `sida2.html`, osv.

---

## Begreppslista – terminologi inom webbutveckling

| Term | Förklaring |
|------|------------|
| **HTML** | HyperText Markup Language – sidans struktur och innehåll |
| **CSS** | Cascading Style Sheets – sidans utseende och layout |
| **JavaScript** | Programmeringsspråk för interaktivitet i webbläsaren |
| **DOM** | Document Object Model – trädstruktur av HTML-element |
| **Element** | En HTML-tagg med innehåll: `<p>Text</p>` |
| **Attribut** | Extra information i en tagg: `<img src="..." alt="...">` |
| **Selektor** | CSS-regel som väljer element: `h1`, `.klass` |
| **Box-modellen** | `content → padding → border → margin` |
| **Flexbox** | Endimensionell layout-modul i CSS |
| **CSS Grid** | Tvådimensionell layout-modul i CSS |
| **Responsiv design** | Layout som anpassas efter skärmstorlek |
| **Viewport** | Den synliga delen av webbsidan |
| **Semantisk HTML** | Element som beskriver innehållets betydelse |
| **Klient** | Webbläsaren som visar sidan |
| **Server** | Datorn som skickar filerna |
| **Protokoll** | HTTP/HTTPS – regler för dataöverföring |
| **URL** | Uniform Resource Locator – webbadress |

---

## Lagar och bestämmelser

I kursen berörs:
- **Tillgänglighet:** `alt`-texter på bilder, semantisk HTML, responsiv design
- **Upphovsrätt:** Bilder från Unsplash (fria att använda), källhänvisningar till Wikipedia och ICA
- **GDPR:** Medvetenhet om att inte samla in personuppgifter via formulär (enbart `prompt()` i utbildningssyfte)

---

## Sammanfattning

Kursen Webbutveckling 1 har gett eleverna en praktisk grund i att:

1. **Skapa webbsidor med HTML5** – från enkla rubriker till tabeller, bilder och formulär
2. **Styla med CSS3** – typografi, färger, box-modellen, flexbox, grid, animationer
3. **Bygga flersidiga webbplatser** – gemensam navigering, konsekvent design
4. **Göra responsiva layouter** – anpassning för mobil, surfplatta och dator
5. **Programmera med JavaScript** – DOM-manipulation, händelser, användarinteraktion
6. **Följa webbstandarder** – korrekt syntax, semantisk HTML, tillgänglighet

Varje kapitel har sin egen `HISTORIK.md` med detaljerad lektionshistorik, begreppslistor och kodexempel.
