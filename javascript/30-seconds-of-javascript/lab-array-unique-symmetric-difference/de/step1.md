# Array Unique Symmetric Difference Funktion

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Die folgende Funktion gibt den einzigartigen symmetrischen Unterschied zwischen zwei Arrays zurück. Sie entfernt doppelte Werte aus einem der beiden Arrays.

Um dies zu erreichen, verwenden Sie `Array.prototype.filter()` und `Array.prototype.includes()` auf jedem Array, um die in dem anderen Array enthaltenen Werte zu entfernen. Erstellen Sie aus den Ergebnissen einen `Set`, um doppelte Werte zu entfernen.

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

Verwenden Sie die Funktion wie folgt:

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
