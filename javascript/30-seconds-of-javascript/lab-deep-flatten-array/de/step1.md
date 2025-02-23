# Wie man in JavaScript ein Array mit Rekursion tiefflacht

Um in JavaScript ein Array tiefflacht, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um das Array zu flachen.
3. Verwenden Sie die `Array.prototype.concat()`-Methode mit einem leeren Array (`[]`) und dem Spread-Operator (`...`), um das Array zu flachen.
4. Flachen Sie jedes Element, das ein Array ist, rekursiv.
5. Implementieren Sie folgenden Code:

```js
const deepFlatten = (arr) =>
  [].concat(...arr.map((v) => (Array.isArray(v) ? deepFlatten(v) : v)));

deepFlatten([1, [2], [[3], 4], 5]); // [1, 2, 3, 4, 5]
```

Indem Sie diesen Schritten folgen, können Sie mit Hilfe von Rekursion in JavaScript leicht ein Array tiefflachen.
