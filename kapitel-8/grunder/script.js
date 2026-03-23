// let lunch = "ärtsoppa"
// alert("Min favoritlunch är " + lunch)
//alert(`Min favoritlunch är ${lunch}`)   // Variabelsubstitution
// let svar = prompt("Vad är din favoritlunch?")

let lön = prompt("Hur mycket tjänade du före skatt?")   // Tex 15000
let skatt = prompt("Vad är din skattesats? (%)")    // Tex 10 
// let netto = lön * (100 - skatt)/100 // 15000 * (100 - 10)/100 = 15000 * 0.9
let netto = parseInt(lön) * (100 - parseInt(skatt))/100 // 15000 * (100 - 10)/100 = 15000 * 0.9

alert(`Din nettolön efter skatt är ${netto}`)