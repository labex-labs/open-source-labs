# Funktion zur Berechnung der Summe der Elemente einer abgebildeten Array

Um die Summe eines Arrays zu berechnen, indem jedes Element mithilfe einer bereitgestellten Funktion einem Wert zugeordnet wird, verwenden Sie die `sumBy`-Funktion. Diese Funktion verwendet `Array.prototype.map()`, um jedes Element dem von `fn` zurückgegebenen Wert zuzuordnen. Anschließend verwendet sie `Array.prototype.reduce()`, um jeden Wert einem Akkumulator hinzuzufügen, der mit einem Wert von `0` initialisiert wird.

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

Beispielverwendung:

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // Gibt 20 zurück
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // Gibt 20 zurück
```

Um mit dieser Funktion zu beginnen, die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
