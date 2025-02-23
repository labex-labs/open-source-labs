# Ein Arraykreuzprodukt in JavaScript erstellen

Um ein Arraykreuzprodukt in JavaScript zu erstellen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, `Array.prototype.map()` und `Array.prototype.concat()`, um jedes mögliche Paar aus den Elementen der beiden Arrays zu erzeugen.
3. Die Funktion `xProd()` nimmt zwei Arrays als Argumente entgegen und erstellt aus den beiden bereitgestellten Arrays ein neues Array, indem sie jedes mögliche Paar aus den Arrays erstellt.
4. Hier ist ein Beispiel für die Funktion `xProd()` im Einsatz:

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

Dies wird ein Array zurückgeben, das alle möglichen Paare von Elementen aus den beiden Eingabearrays enthält.
