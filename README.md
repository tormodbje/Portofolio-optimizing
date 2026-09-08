# 📈 Bygg deres egen portefølje

## Om prosjektet

Dette prosjektet etablerer et hypotetisk investeringsfond og undersøker hvordan ulike porteføljekonstruksjoner påvirkes av forventet avkastning, risiko og korrelasjon mellom aktiva.

Fondet investerer i **20–50 aksjer, ETF-er eller andre likvide aktiva**. Gjennom prosjektet konstrueres, optimaliseres og sammenlignes flere typer porteføljer basert på historiske markedsdata.

Prosjektet gir en praktisk introduksjon til **porteføljeoptimalisering og risikostyring**, samtidig som det demonstrerer matematisk optimalisering i praksis.

---

## 🎯 Hovedmål

Konstruere og sammenligne flere typer porteføljer basert på historiske data og ulike optimeringskriterier, samt undersøke:

- Hvor mye porteføljeoptimalisering faktisk betyr for risiko og avkastning
- Om avanserte optimeringsmodeller gir bedre resultater enn en enkel **1/N-portefølje**
- Stabiliteten i porteføljevekter når parametere endres
- Følsomheten av klassiske modeller overfor usikre parameterestimater

---

## 📊 Porteføljer

### 1. Likevektet portefølje (1/N)

Hvert aktivum får samme vekt:

$$w_i = \frac{1}{N}$$

der $N$ er antall aktiva. Fungerer som enkel referanseportefølje.

**Hvordan det fungerer:**
- Beregn antall aktiva $N$ i investeringsuniverset
- Tildel hver aksje vekten $\frac{1}{N}$ (f.eks. 2% hver hvis $N = 50$)
- Ingen optimalisering – ren mekanisk fordeling

**Fordeler:** Enkel, ingen skjemte estimater, robust mot modellfeil  
**Ulemper:** Ignorerer risiko og korrelasjoner

---

### 2. Minimum-varians-portefølje

Porteføljen konstrueres for å minimere forventet porteføljevarians:

$$\min_w \quad w^T\Sigma w$$

**Hvordan det fungerer:**
1. Beregn historisk kovariansmatrise $\Sigma$ fra prisdata
2. Bruk kvadratisk programmering (QP) for å finne vektene $w$ som minimerer varians
3. Ofte legges begrensninger på: $\sum w_i = 1$, og eventuelt $w_i \geq 0$ (no short-selling)

**Matematisk prosess:**
- Startpunkt: tilfeldig portefølje
- Algoritmen justerer vektene iterativt
- Stopp når ytterligere endringer øker variansen

**Fordeler:** Minimerer risiko, stabil strategi  
**Ulemper:** Ignorerer avkastningsforventninger, kan bli konsentrert i få aktiva

---

### 3. Maksimum-Sharpe-portefølje

Denne porteføljen maksimerer risikojustert avkastning (Sharpe-raten):

$$\max_w \quad \frac{w^T\mu - r_f}{\sqrt{w^T\Sigma w}}$$

der:
- $w$ = vektor med porteføljevekter
- $\mu$ = forventet avkastning (historisk gjennomsnitt)
- $\Sigma$ = kovariansmatrise
- $r_f$ = risikofri rente

**Hvordan det fungerer:**
1. Beregn gjennomsnittlig avkastning $\mu$ for hvert aktivum
2. Beregn kovariansmatrise $\Sigma$
3. Bruk optimalisering for å finne vektene som maksimerer: $\frac{\text{Meravkastning}}{\text{Risiko}}$
4. Resultatet er den porteføljen med best avkastning per enhet risiko

**Matematisk intuisjon:**
- Telleren: hvor mye ekstra avkastning du får over risikofri rente
- Nevneren: hvor mye risiko du tar
- Maksimere forholdet = best pris per risiko

**Fordeler:** Balanserer risiko og avkastning optimalt  
**Ulemper:** Veldig følsom for estimeringsusikkerhet i $\mu$

---

### 4. Risiko-paritet-portefølje

Fordeler porteføljens risiko mer jevnt mellom aktivaene, fremfor å fordele kapitalen likt.

**Hvordan det fungerer:**
1. Beregn volatilitet $\sigma_i = \sqrt{\Sigma_{ii}}$ for hvert aktivum
2. Tildel vekt omvendt proporsjonal med volatilitet: $w_i \propto \frac{1}{\sigma_i}$
3. Normalisér slik at $\sum w_i = 1$

**Eksempel:**
- Aktivum A: volatilitet 10% → høy vekt
- Aktivum B: volatilitet 20% → lavere vekt
- Aktivum C: volatilitet 5% → høyest vekt

**Intuisjon:** Høyrisikoaktiva får mindre penger, lavrisiko-aktiva får mer, slik at hver aksje bidrar omtrent likt til porteføljens totale risiko.

**Fordeler:** Balansert risikofordeling, intuitiv strategi  
**Ulemper:** Ignorerer avkastningsforventninger og korrelasjoner

---

## 🧮 Matematisk grunnlag

### Porteføljestatistikk

For en portefølje med vekter $w$, forventede avkastninger $\mu$ og kovariansmatrise $\Sigma$:

**Forventet porteføljeAvkastning:**
$$E[R_p] = w^T\mu$$

**Porteføljens varians:**
$$\sigma_p^2 = w^T\Sigma w$$

**Porteføljens volatilitet (standardavvik):**
$$\sigma_p = \sqrt{w^T\Sigma w}$$

**Sharpe-ratio:**
$$\text{Sharpe} = \frac{E[R_p] - r_f}{\sigma_p}$$

### Kovariansmatrisen

Kovariansmatrisen $\Sigma$ måler hvordan aktivaene beveger seg sammen:

$$\Sigma_{ij} = \text{Cov}(R_i, R_j)$$

**Hvordan den beregnes:**
1. Ta historiske avkastninger for hver aksje
2. Beregn gjennomsnittsavkastning
3. Beregn avvik fra gjennomsnitt for hver dag
4. Multipliser avvikene og ta gjennomsnitt

**Eksempel:**
- Hvis aksje A og B alltid stiger sammen: høy positiv kovarians
- Hvis de beveger seg motsatt: negativ kovarians
- Diversifisering fungerer fordi negative korrelasjoner reduserer risiko

---

## 📈 Data og implementasjon

### 1. **Datainnsamling**

```python
import yfinance as yf
import pandas as pd

# Hent historiske data
tickers = ['AAPL', 'MSFT', 'GOOGL', ...]  # 20-50 aksjer
data = yf.download(tickers, start='2020-01-01', end='2024-01-01')['Adj Close']