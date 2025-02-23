# Überprüfen, ob ein Wert eine asynchrone Funktion in JavaScript ist

Um zu überprüfen, ob ein Wert eine `async`-Funktion in JavaScript ist, können Sie folgenden Code verwenden:

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

Diese Funktion verwendet `Object.prototype.toString()` und `Function.prototype.call()`, um zu überprüfen, ob das gegebene Argument eine `async`-Funktion ist.

Sie können die Funktion testen, indem Sie eine reguläre Funktion und eine `async`-Funktion als Argumente übergeben:

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

Um zu beginnen, JavaScript zu programmieren, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
