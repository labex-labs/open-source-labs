# Wie man mithilfe von JavaScript den Index des letzten übereinstimmenden Elements in einem Array findet

Um den Index des letzten Elements zu finden, das einer bestimmten Bedingung in einem JavaScript-Array entspricht, verwenden Sie die `findLastIndex`-Funktion. Hier ist, wie man sie verwendet:

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

Die `findLastIndex`-Funktion nimmt zwei Argumente entgegen: das Array, in dem gesucht werden soll, und eine Funktion, um jedes Element zu testen. Hier ist, wie es funktioniert:

1. Verwenden Sie `Array.prototype.map()`, um ein neues Array aus `[Index, Wert]`-Paaren zu erstellen.
2. Verwenden Sie `Array.prototype.filter()`, um Elemente aus dem Array zu entfernen, die der Bedingung, die von der `fn`-Funktion bereitgestellt wird, nicht entsprechen.
3. Verwenden Sie `Array.prototype.pop()`, um das letzte Element im gefilterten Array zu erhalten.
4. Wenn das gefilterte Array leer ist, geben Sie `-1` zurück.

Hier ist ein Beispiel, wie man `findLastIndex` verwendet:

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (Index des Werts 3)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (Standardwert, wenn nicht gefunden)
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
