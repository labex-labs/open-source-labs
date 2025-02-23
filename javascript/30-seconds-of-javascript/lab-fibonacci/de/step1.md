# Fibonacci-Folge

Um die Fibonacci-Folge in JavaScript zu generieren, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein.
2. Verwenden Sie `Array.from()`, um ein leeres Array der bestimmten Länge zu erstellen und die ersten beiden Werte (`0` und `1`) zu initialisieren.
3. Verwenden Sie `Array.prototype.reduce()` und `Array.prototype.concat()`, um Werte zum Array hinzuzufügen, wobei Sie die Summe der letzten beiden Werte verwenden, außer für die ersten beiden.
4. Rufen Sie die `fibonacci()`-Funktion auf und übergeben Sie die gewünschte Länge der Sequenz als Argument.

Hier ist der Code:

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

Dies wird ein Array generieren, das die Fibonacci-Folge bis zum n-ten Glied enthält.
