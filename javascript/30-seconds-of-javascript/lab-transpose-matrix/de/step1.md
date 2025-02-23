# Matrix in JavaScript transponieren

Um ein zweidimensionales Array in JavaScript zu transponieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.map()`, um die Transposition des gegebenen zweidimensionalen Arrays zu erstellen. Die `map()`-Methode erstellt ein neues Array mit den Ergebnissen des Aufrufs einer bereitgestellten Funktion für jedes Element im Array.
3. Die bereitgestellte Funktion sollte zwei Argumente akzeptieren: das aktuelle Element des Arrays und dessen Index. In diesem Fall benötigen wir nur den Index, um die Transposition zu erstellen.
4. Verwenden Sie den Index, um auf die entsprechenden Elemente in jeder Zeile des zweidimensionalen Arrays zuzugreifen und ein neues Array mit diesen Elementen zu erstellen. Dies wird die neue Zeile im transponierten Array sein.
5. Wiederholen Sie den vorherigen Schritt für jede Spalte im zweidimensionalen Array, um das vollständige transponierte Array zu erstellen.

Hier ist der Code, um ein zweidimensionales Array in JavaScript zu transponieren:

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
