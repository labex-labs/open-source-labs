# Wie man den Einfügeindex in einem sortierten Array findet

Um den niedrigsten Index zu finden, an dem ein Wert in ein sortiertes Array eingefügt werden sollte, folgen Sie diesen Schritten:

1. Überprüfen Sie, ob das Array in absteigender Reihenfolge sortiert ist.
2. Verwenden Sie die `Array.prototype.findIndex()`-Methode, um den passenden Index zu finden, an dem das Element eingefügt werden sollte.

Hier ist der Code, um dies umzusetzen:

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

Sie können die `sortedIndex`-Funktion aufrufen, indem Sie das sortierte Array und den Wert übergeben, den Sie einfügen möchten. Hier sind einige Beispiele:

```js
sortedIndex([5, 3, 2, 1], 4); // Ausgabe: 1
sortedIndex([30, 50], 40); // Ausgabe: 1
```

Mit dieser Funktion können Sie leicht den Einfügeindex eines Werts in einem sortierten Array finden.
