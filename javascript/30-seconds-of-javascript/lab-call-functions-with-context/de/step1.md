# Wie man in JavaScript Funktionen mit einem Kontext aufruft

Um Code in Node.js auszuführen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Wenn Sie in JavaScript eine Funktion mit einem bestimmten Kontext und einer Menge von Argumenten aufrufen möchten, können Sie eine Closure verwenden. Hier ist, wie Sie es tun können:

1. Definieren Sie eine Funktion namens `call`, die einen `Schlüssel` und eine Menge von `Argumenten` als Parameter nimmt und eine neue Funktion zurückgibt, die einen `Kontext`-Parameter nimmt.

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. Verwenden Sie die `call`-Funktion, um die `map`-Funktion auf einem Array von Zahlen aufzurufen. In diesem Beispiel verdoppelt die `map`-Funktion jede Zahl im Array.

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. Sie können die `call`-Funktion auch an einen bestimmten Schlüssel wie `map` binden und sie verwenden, um die `map`-Funktion auf einem Array von Zahlen aufzurufen.

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

Durch die Verwendung der `call`-Funktion können Sie leicht jede Funktion mit einem bestimmten Kontext und einer Menge von Argumenten aufrufen.
