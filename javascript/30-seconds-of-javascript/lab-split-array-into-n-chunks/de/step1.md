# Wie man ein Array in N Blöcke aufteilt

Um ein Array in `n` kleinere Arrays aufzuteilen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Math.ceil()` und `Array.prototype.length`, um die Größe jedes Blocks zu berechnen.
3. Verwenden Sie `Array.from()`, um ein neues Array der Größe `n` zu erstellen.
4. Verwenden Sie `Array.prototype.slice()`, um jedes Element des neuen Arrays auf einen Block der Länge `size` abzubilden.
5. Wenn das ursprüngliche Array nicht gleichmäßig aufgeteilt werden kann, enthält der letzte Block die verbleibenden Elemente.

Hier ist eine Beispiel-Implementierung der `chunkIntoN`-Funktion in JavaScript:

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

Sie können diese Funktion verwenden, um ein Array in `n` Blöcke aufzuteilen, indem Sie das Array und die gewünschte Anzahl von Blöcken als Argumente übergeben. Beispiel:

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
