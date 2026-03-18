// let justNu = new Date();
// console.log(justNu);

// let ar = nu.getFullYear(); // Hämtar året med fyra siffror (t.ex. 2026)
// let dag = nu.getDate();    // Hämtar dagens datum (1-31)
// let veckodag = nu.toLocaleDateString('de-DE', {weekday: 'long'})
// let månad = nu.toLocaleDateString('de-DE', {month: 'long'})
// console.log("Nu är det år " + ar);
// alert("Nu är det år " + ar)
// document.querySelector('h1').textContent = "Nu är det år " + ar
// document.querySelector('h2').textContent = "Idag är det " + veckodag + " "+ dag + " " + månad
function visaKlocka() {
    let nu = new Date();
    let timmar = nu.getHours()
    let minuter = nu.getMinutes()
    let sekunder = nu.getSeconds()
    document.querySelector('h3').textContent = timmar + ":" + minuter + ":" + sekunder
}
setInterval(visaKlocka, 1000)