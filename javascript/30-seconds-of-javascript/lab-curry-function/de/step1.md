# Ein Funktionsargument kümmern

Um eine Funktion zu kümmern, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion.
3. Überprüfen Sie, ob die Anzahl der bereitgestellten Argumente (`args`) ausreicht.
4. Wenn ja, rufen Sie die übergebene Funktion `fn` auf.
5. Wenn nicht, verwenden Sie `Function.prototype.bind()`, um eine gekümmerte Funktion `fn` zurückzugeben, die die restlichen Argumente erwartet.
6. Wenn Sie eine Funktion kümmern möchten, die eine variable Anzahl von Argumenten akzeptiert (eine variadische Funktion, z.B. `Math.min()`), können Sie optional die Anzahl der Argumente als zweites Parameter `arity` übergeben.
7. Verwenden Sie folgenden Code:

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

Hier sind einige Beispiele:

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
