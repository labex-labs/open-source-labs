# Wie man den letzten Einfügeindex in einem sortierten Array basierend auf einer Funktion findet

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist, wie man den höchsten Index findet, an dem ein Wert in ein Array eingefügt werden sollte, um seine Sortierreihenfolge beizubehalten, basierend auf einer bereitgestellten Iterationsfunktion:

1. Überprüfen Sie, ob das Array in absteigender Reihenfolge sortiert ist.
2. Verwenden Sie `Array.prototype.map()`, um die Iterationsfunktion auf alle Elemente des Arrays anzuwenden.
3. Verwenden Sie `Array.prototype.reverse()` und `Array.prototype.findIndex()`, um den passenden letzten Index zu finden, an dem das Element eingefügt werden sollte, basierend auf der bereitgestellten Iterationsfunktion.

Siehe den folgenden Code:

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Hier ist ein Beispiel:

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
