# Wie man in JavaScript die leistungsfähigste Funktion findet

Um in JavaScript die leistungsfähigste Funktion zu finden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.map()`, um ein Array zu generieren, wobei jeder Wert die Gesamtzeit angibt, die es dauert, die Funktion `iterations` Mal auszuführen.
3. Nutzen Sie die Differenz der `performance.now()`-Werte vor und nach der Ausführung, um die Gesamtzeit in Millisekunden mit hoher Genauigkeit zu erhalten.
4. Verwenden Sie `Math.min()`, um die minimale Ausführungszeit zu finden, und geben Sie den Index dieser kürzesten Zeit zurück, der dem Index der leistungsfähigsten Funktion entspricht.
5. Wenn Sie das zweite Argument `iterations` weglassen, verwendet die Funktion als Standard `10000` Iterationen.
6. Denken Sie daran, dass je mehr Iterationen Sie verwenden, desto zuverlässiger ist das Ergebnis, aber auch länger wird es dauern.

Hier ist ein Beispielcodeausschnitt:

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

Um diese Funktion zu verwenden, übergeben Sie als erstes Argument ein Array von Funktionen und als zweites Argument (optional) die Anzahl der Iterationen. Beispiel:

```js
mostPerformant([
  () => {
    // Geht durch das gesamte Array, bevor `false` zurückgegeben wird
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // Muss nur bis zum Index `1` gelangen, bevor `false` zurückgegeben wird
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
