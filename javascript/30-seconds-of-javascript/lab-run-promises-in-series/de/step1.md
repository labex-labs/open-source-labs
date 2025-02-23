# Promises nacheinander ausführen

Um eine Reihe von Promises nacheinander auszuführen, verwenden Sie `Array.prototype.reduce()`, um eine Promise-Kette zu erstellen. Jedes Promise gibt das nächste Promise nach der Auflösung zurück.

Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

Hier ist ein Beispiel für den Code:

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

Sie können dann die `runPromisesInSeries`-Funktion verwenden, um Promises sequentiell auszuführen, wie im folgenden Beispiel gezeigt:

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// Dieser Code führt jedes Promise nacheinander aus und benötigt insgesamt 3 Sekunden, bis er abgeschlossen ist.
```
