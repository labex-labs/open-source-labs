# Wie man in JavaScript eine Potenzmenge generiert

Um in JavaScript eine Potenzmenge eines gegebenen Arrays von Zahlen zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Methode `Array.prototype.reduce()`, kombiniert mit der Methode `Array.prototype.map()`, um über die Elemente zu iterieren und sie zu einem Array zu kombinieren, das alle Kombinationen enthält.
3. Implementieren Sie folgenden Code:

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. Um die Potenzmenge zu generieren, rufen Sie die Funktion `powerset()` auf und übergeben das Array als Argument. Beispiel:

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

Dies wird ein Array zurückgeben, das alle möglichen Teilmengen des gegebenen Arrays enthält.
