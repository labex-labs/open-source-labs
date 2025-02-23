# Beschreibung des letzten Einfügeindex in einem sortierten Array

Um den höchsten Index zu finden, an dem ein Wert in ein Array eingefügt werden sollte, um seine Sortierreihenfolge beizubehalten, folgen Sie diesen Schritten:

- Überprüfen Sie zunächst grob, ob das Array in absteigender Reihenfolge sortiert ist.
- Verwenden Sie dann `Array.prototype.reverse()` und `Array.prototype.findIndex()`, um den passenden letzten Index zu finden, an dem das Element eingefügt werden sollte.

Hier ist der Code für die Funktion:

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Und hier ist ein Beispiel dafür, wie die Funktion verwendet wird:

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
