# Eine Funktion, die eine andere Funktion aufruft oder zurückgibt

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Funktion namens `callOrReturn`, die ein Argument nimmt und es aufruft, wenn es eine Funktion ist, andernfalls gibt es es zurück. So funktioniert es:

- Die Funktion nimmt zwei Parameter: `fn` und `...args`. `fn` ist das zu überprüfende Argument, und `...args` ist die Liste der Argumente, die an die Funktion übergeben werden sollen, wenn diese aufgerufen wird.
- Sie verwendet den `typeof`-Operator, um zu überprüfen, ob das gegebene Argument eine Funktion ist.
- Wenn das Argument tatsächlich eine Funktion ist, ruft sie die Funktion mit dem Spread-Operator (`...`) auf, um die restlichen gegebenen Argumente zu übergeben. Andernfalls gibt sie das Argument einfach zurück.
- Hier ist ein Beispiel, wie die `callOrReturn`-Funktion verwendet werden kann:

```js
const callOrReturn = (fn, ...args) =>
  typeof fn === "function" ? fn(...args) : fn;

callOrReturn((x) => x + 1, 1); // 2
callOrReturn(1, 1); // 1
```

Im ersten Beispiel ruft `callOrReturn(x => x + 1, 1)` die Funktion `x => x + 1` mit dem Argument `1` auf, was `2` zurückgibt. Im zweiten Beispiel gibt `callOrReturn(1, 1)` einfach `1` zurück, da es keine Funktion ist.
