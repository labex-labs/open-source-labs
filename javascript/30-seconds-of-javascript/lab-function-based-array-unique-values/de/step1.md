# Das Finden von einzigartigen Werten in einem Array mit einer Funktion

Um alle einzigartigen Werte eines Arrays zu finden, muss eine Vergleichsfunktion bereitgestellt werden.

Verwenden Sie `Array.prototype.reduce()` und `Array.prototype.some()`, um ein Array zu erstellen, das nur das erste einzigartige Vorkommen jedes Werts enthält. Die Vergleichsfunktion `fn` nimmt zwei Argumente, die Werte der beiden zu vergleichenden Elemente.

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

Um die Funktion zu testen, verwenden Sie das folgende Beispiel:

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

Beginnen Sie mit der Praxis des Codierens, indem Sie das Terminal/SSH öffnen und `node` eingeben.
