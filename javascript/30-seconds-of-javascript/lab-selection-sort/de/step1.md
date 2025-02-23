# Auswahlsortieralgorithmus

Um zu beginnen, den Code zu schreiben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die folgende Funktion sortiert ein Array von Zahlen mit dem Auswahlsortieralgorithmus:

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

Um die Funktion zu verwenden, übergeben Sie ein Array von Zahlen an `selectionSort()`, wie folgt:

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

Die Funktion funktioniert, indem sie das ursprüngliche Array mit dem Spread-Operator (`...`) klont. Anschließend iteriert sie über das Array mit einer `for-Schleife`. Mit `Array.prototype.slice()` und `Array.prototype.reduce()` findet sie den Index des kleinsten Elements im Teilarray rechts vom aktuellen Index. Wenn erforderlich, führt sie einen Tausch durch.
