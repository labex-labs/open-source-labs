# Funktionsfrequenzberechnung

Um die Frequenz der Ausführung einer Funktion pro Sekunde (hz/hertz) zu messen, verwenden Sie die `hz`-Funktion. Sie können dies tun, indem Sie die folgenden Schritte ausführen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `performance.now()`, um die Differenz in Millisekunden vor und nach der Iterationsschleife zu erhalten, um die vergangene Zeit bei der Ausführung der Funktion `iterations`-mal zu berechnen.
3. Konvertieren Sie Millisekunden in Sekunden und dividieren Sie sie durch die vergangene Zeit, um die Anzahl der Zyklen pro Sekunde zurückzugeben.
4. Wenn Sie die Standardeinstellung von 100 Iterationen verwenden möchten, lassen Sie den zweiten Argument `iterations` weg.

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

Hier ist ein Beispiel für die Verwendung der `hz`-Funktion, um die Leistung von zwei Funktionen zu vergleichen, die die Summe eines Arrays von 10.000 Zahlen berechnen:

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

In diesem Beispiel ist `sumReduce` schneller als `sumForLoop`, weil es eine niedrigere Frequenz der Funktionsausführung hat.
