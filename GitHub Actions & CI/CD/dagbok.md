## Uppdatering av AI-modell i GitHub Actions

Vi har gjort en viktig justering i vår automatiska dokumentationsprocess som påverkar vilken AI-modell som används.

### Vad ändrades?
Vi har uppdaterat miljövariabeln `GEMINI_MODEL` i vår GitHub Actions-workflow (`.github/workflows/auto-docs.yml`). Den tidigare modellen `gemini-3-flash-preview` har nu ersatts med `gemini-2.5-flash`.

### Varför ändrades det?
`gemini-2.5-flash` är en snabb och kostnadseffektiv modell som är väl lämpad för att generera text och sammanfatta information, vilket är huvudsyftet med vårt dokumentationsskript. Att välja rätt AI-modell handlar ofta om att balansera faktorer som prestanda, kostnad och tillgänglighet. Denna ändring syftar till att optimera vår process för att vara både effektiv och ekonomisk.

### Var hittar vi detta?
Ändringen gjordes i filen `.github/workflows/auto-docs.yml`, som definierar stegen för vårt CI/CD-flöde (Continuous Integration/Continuous Deployment). Specifikt ändrades raden som sätter miljövariabeln `GEMINI_MODEL` under jobbet `generate-documentation`.

### Viktigt att veta
I modern webbutveckling, speciellt med CI/CD-pipelines, är det vanligt att kontinuerligt justera konfigurationer. Detta kan vara för att förbättra effektiviteten, anpassa sig till nya verktyg, eller dra nytta av uppdaterade AI-modeller som erbjuder bättre prestanda eller lägre kostnad.