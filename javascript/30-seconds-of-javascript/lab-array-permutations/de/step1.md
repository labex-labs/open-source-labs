# Wie man alle Array-Permutationen generiert

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist ein Algorithmus, der alle Permutationen der Elemente eines Arrays generiert (auch wenn es Duplikate enthält). Folgen Sie diesen Schritten, um ihn zu implementieren:

1. Verwenden Sie Rekursion.
2. Für jedes Element im gegebenen Array erstellen Sie alle partiellen Permutationen für die restlichen Elemente.
3. Verwenden Sie `Array.prototype.map()`, um das Element mit jeder partiellen Permutation zu kombinieren, und dann `Array.prototype.reduce()`, um alle Permutationen in einem Array zu kombinieren.
4. Die Basisfälle sind für Arrays mit einer Länge von `2` oder `1`.
5. Achten Sie darauf, dass die Ausführungszeit dieser Funktion exponentiell mit jedem Array-Element zunimmt. Mehr als 8 bis 10 Einträge können dazu führen, dass Ihr Browser hängt, wenn er versucht, alle verschiedenen Kombinationen zu lösen.

Hier ist der Code:

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val
        ])
      ),
    []
  );
};
```

Sie können den Code testen, indem Sie die `permutations()`-Funktion mit einem Array-Argument aufrufen:

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
