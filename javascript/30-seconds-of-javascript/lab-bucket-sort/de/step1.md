# Bucket-Sort-Algorithmus

Um den Bucket-Sort-Algorithmus zu verwenden und ein Array von Zahlen zu sortieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Finden Sie den kleinsten und größten Wert des gegebenen Arrays mithilfe von `Math.min()`, `Math.max()` und dem Spread-Operator (`...`).
3. Erstellen Sie die passende Anzahl von `Buckets` (leere Arrays) mithilfe von `Array.from()` und `Math.floor()`.
4. Befüllen Sie jedes Bucket mit den passenden Elementen aus dem Array mithilfe von `Array.prototype.forEach()`.
5. Sortieren Sie jedes Bucket und fügen Sie es zum Ergebnis hinzu mithilfe von `Array.prototype.reduce()`, dem Spread-Operator (`...`) und `Array.prototype.sort()`.

Hier ist eine Beispielimplementierung des Bucket-Sort-Algorithmus in JavaScript:

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => []
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

Um den Algorithmus zu testen, führen Sie folgenden Code aus:

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
