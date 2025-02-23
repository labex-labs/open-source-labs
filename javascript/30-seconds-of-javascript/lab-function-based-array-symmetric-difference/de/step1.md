# Eine Funktion zur Suche nach der symmetrischen Differenz von Arrays

Um die symmetrische Differenz zwischen zwei Arrays mithilfe einer bereitgestellten Funktion als Vergleichsmethode zu finden, folgen Sie diesen Schritten:

1. Öffnen Sie die Konsole/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
2. Verwenden Sie die Methoden `Array.prototype.filter()` und `Array.prototype.findIndex()`, um die passenden Werte zu finden.
3. Verwenden Sie den bereitgestellten Code, um die Operation durchzuführen.

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

Beispielsweise betrachten Sie die folgende Eingabe:

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

Der obige Code wird `[1, 1.2, 3.9]` als symmetrische Differenz zwischen den beiden Arrays zurückgeben.
