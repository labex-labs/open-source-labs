# Überprüfen, ob Array - Elemente mit einer gegebenen Funktion gleich sind

Um zu überprüfen, ob alle Elemente in einem Array gleich sind, verwenden Sie die `allEqualBy` - Funktion. Diese Funktion wendet eine gegebene Abbildung (Mapping) - Funktion `fn` auf das erste Element des Arrays `arr` an. Anschließend überprüft sie, ob `fn` für alle Elemente im Array denselben Wert zurückgibt wie für das erste Element, indem sie `Array.prototype.every()` verwendet. Die Funktion verwendet den strikten Vergleichsoperator, der die `NaN` - Selbstungleichheit nicht berücksichtigt.

Hier ist der Code für `allEqualBy`:

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

Sie können `allEqualBy` wie folgt verwenden:

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

Um mit dieser Funktion an der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
