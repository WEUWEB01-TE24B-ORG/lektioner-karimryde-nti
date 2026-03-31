document.querySelector(".musik").play()

// Kod som körs direkt när sidan laddas
let vinkel = 0

// Kod som körs när jag klickar på knappen
function roteraBild() {
    vinkel += 90
    document.querySelector("img").style.transform = "rotate(+" + vinkel + "deg)"
}

function spelaLjud() {
    document.querySelector(".beep").play()
    document.querySelector(".musik").pause()
}

// Gömma med display = "none"
// Visa med display = "block"
function visaVideo() {
    document.querySelector(".video-lada").style.display = "block"
}