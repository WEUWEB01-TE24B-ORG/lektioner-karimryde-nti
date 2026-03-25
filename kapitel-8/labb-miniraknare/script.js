function addera() {
    // Läs av första input-rutan
    let tal1 = document.querySelector(".tal1").value
    // Läs av andra input-rutan
    let tal2 = document.querySelector(".tal2").value
    let summa = Number(tal1) + Number(tal2)
    // Skriv ut ett svar i p.resultat
    document.querySelector(".resultat").textContent = "Summan är = " + summa

    // Resultat är positivt grön bakgrund
    // Annrs om negativt röd bakgrund
    if (summa == 0) { // = 0
        document.querySelector(".resultat-ruta").style.backgroundColor = "yellow"
    }
    else if (summa > 0) { // > 0
        document.querySelector(".resultat-ruta").style.backgroundColor = "green"
    } else { // < 0
        document.querySelector(".resultat-ruta").style.backgroundColor = "red"
    }
}