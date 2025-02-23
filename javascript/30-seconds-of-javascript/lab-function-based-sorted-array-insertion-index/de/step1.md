# Funktion zum Finden des Einfügeindex in einem sortierten Array

Um den niedrigsten Index zu finden, an dem ein Wert in einem Array eingefügt werden kann, um die Sortierreihenfolge beizubehalten, verwenden Sie die Funktion `sortedIndexBy(arr, n, fn)` in JavaScript.

Diese Funktion überprüft grob, ob das Array in absteigender Reihenfolge sortiert ist, und verwendet dann `Array.prototype.findIndex()`, um den passenden Index basierend auf der Iterationsfunktion `fn` zu finden.

Hier ist der Code für die `sortedIndexBy()`-Funktion:

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

Sie können die Funktion mit einem Array von Objekten, einem einzufügenden Wert und einer Iterationsfunktion aufrufen.

Beispielsweise gibt `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` `0` zurück, was der Index ist, an dem das `{ x: 4 }`-Objekt eingefügt werden sollte, um die Sortierreihenfolge basierend auf der `x`-Eigenschaft beizubehalten.
