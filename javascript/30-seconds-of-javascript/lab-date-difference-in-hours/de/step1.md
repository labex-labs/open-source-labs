# JavaScript-Funktion zur Berechnung der Datumsdifferenz in Stunden

Um die Differenz zwischen zwei Daten in Stunden mit JavaScript zu berechnen, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie die folgende JavaScript-Funktion, um die Differenz (in Stunden) zwischen zwei `Date`-Objekten zu erhalten:

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. Rufen Sie die Funktion mit den beiden Daten als Argumenten auf, um die Differenz in Stunden zu erhalten:

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
