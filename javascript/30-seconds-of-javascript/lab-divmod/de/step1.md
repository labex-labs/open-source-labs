# Codeübung: Quotient und Rest der Division

Um die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dieser Code gibt ein Array zurück, das aus dem Quotienten und dem Rest der angegebenen Zahlen besteht.

Um den Quotienten der Division `x / y` zu erhalten, verwenden Sie `Math.floor()`. Um den Rest der Division `x / y` zu erhalten, verwenden Sie den Modulo-Operator (`%`).

```js
const divmod = (x, y) => [Math.floor(x / y), x % y];
```

Beispiel:

```js
divmod(8, 3); // [2, 2]
divmod(3, 8); // [0, 3]
divmod(5, 5); // [1, 0]
```
