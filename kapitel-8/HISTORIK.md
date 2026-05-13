# Kapitel 8 – JavaScript-introduktion, DOM-manipulation och händelser

Här är historiken över allt vi gjort i detta kapitel. Kapitlet introducerar programmering med JavaScript i webbläsaren. Medvetet begränsat till grundläggande byggstenar: `let`, `if`/`else`, `querySelector`, `.textContent`, `.value`, `.classList`, `Number()`, `prompt()`, `alert()` och namngivna funktioner via `onclick`.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| – | intro | Första mötet med JavaScript: `alert()`, `prompt()`, `document.writeln()`. Strängkonkatenering och template-strings. |
| – | grunder | Byggt en nettolöneberäknare: `let`, `prompt()`, `parseInt()`, matematisk beräkning, `alert()` med template-string. |
| – | onclick | Klick-händelser: `onclick` direkt i HTML på `<h1>` och `<button>`. Ändrat `document.body.style.backgroundColor` vid klick. |
| – | labb-datum | Live-uppdaterande digital klocka: `new Date()`, `.getHours()`, `.getMinutes()`, `.getSeconds()`, `setInterval()`, `document.querySelector('h3').textContent`. |
| – | labb-miniraknare | Byggt en miniräknare med input-fält och knappar: `Number()`, `.value`, `.textContent`, `if`/`else if`/`else` för färgkodning. Dark-theme UI. |
| – | silly-walk | Interaktiv sida: bildrotation (`style.transform`), ljud (`play()`/`pause()`), visa/göm video (`style.display`). |

---

## Begrepp vi lärt oss

### JavaScript
`let`, `if`/`else if`/`else`, `function()`, `onclick`, `document.querySelector()`, `.textContent`, `.value`, `.style`, `.classList`, `Number()`, `parseInt()`, `prompt()`, `alert()`, `console.log()`, `new Date()`, `setInterval()`, template-strings (`` ` ${} ` ``), strängkonkatenering (`+`), `play()`/`pause()`

---

## Exempel från lektionerna

### Första JavaScript (intro)
```javascript
let namn = prompt("Vad heter du?");
document.writeln("Hej " + namn);
```

### Nettolöneberäknare (grunder)
```javascript
let lön = parseInt(prompt("Vad är din bruttolön?"));
let skatt = parseInt(prompt("Vad är din skattesats?"));
let netto = lön * (100 - skatt) / 100;
alert(`Din nettolön efter skatt är ${netto}`);
```

### Klick-händelse (onclick)
```html
<h1 onclick="kaboom()">Klick-händelser</h1>
<button onclick="liteKod()">Klicka inte på mig!</button>
```
```javascript
function kaboom() {
    document.body.style.backgroundColor = "red";
}
function liteKod() {
    alert("Oh nej, du klickade ändå!");
}
```

### Digital klocka (labb-datum)
```javascript
function visaKlocka() {
    let nu = new Date();
    let tim = nu.getHours();
    let min = nu.getMinutes();
    let sek = nu.getSeconds();
    document.querySelector('h3').textContent = tim + ":" + min + ":" + sek;
}
setInterval(visaKlocka, 1000);
```

### Miniräknare med färgkodning (labb-miniraknare)
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

### Bildrotation och ljud (silly-walk)
```javascript
let vinkel = 0;

function roteraBild() {
    vinkel += 90;
    document.querySelector("img").style.transform = "rotate(" + vinkel + "deg)";
}
function spelaLjud() {
    document.querySelector(".beep").play();
}
function visaVideo() {
    document.querySelector(".video-lada").style.display = "block";
}
```

---

## Viktiga detaljer

- **Hård begränsning:** Endast `let` (inte `const`/`var`), inga loopar, arrayer, objekt eller `addEventListener`.
- `onclick`-attribut i HTML används för händelsehantering – inte `addEventListener`.
- `<script src="script.js">` placeras **alltid sist i `<body>`**, aldrig i `<head>`.
- `Number()` och `parseInt()` används för att konvertera text (från `.value` eller `prompt()`) till siffror.
- Template-strings (`` ` ${} ` ``) är ett modernt sätt att bygga strängar med variabler.
- `.textContent` ändrar textinnehåll, `.value` läser input-fält, `.style` ändrar CSS direkt.
- Alla funktioner är namngivna (t.ex. `function addera()`) – inga anonyma funktioner.
- `setInterval()` anropar en funktion med jämna mellanrum (t.ex. varje sekund för en klocka).
