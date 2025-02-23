# Prüfen auf Gleichheit von Array-Elementen

Um zu prüfen, ob alle Elemente in einem Array gleich sind, können Sie die `Array.prototype.every()`-Methode verwenden, die alle Elemente mit dem ersten vergleicht.

So können Sie es implementieren:

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

Beachten Sie, dass der `strenge Vergleichs`-Operator verwendet wird, um die Elemente zu vergleichen. Dieser Operator berücksichtigt die Selbstungleichheit von `NaN` nicht.

Beispielverwendung:

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
