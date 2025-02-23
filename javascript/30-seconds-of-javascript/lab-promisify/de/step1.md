# Promisify-Funktion

Um eine asynchrone Funktion zu konvertieren, um eine Promise zurückzugeben, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie Currying, um eine Funktion zurückzugeben, die eine `Promise` zurückgibt, die die ursprüngliche Funktion aufruft.
3. Verwenden Sie den Rest-Operator (`...`), um alle Parameter zu übergeben.
4. Wenn Sie Node 8+ verwenden, können Sie [`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original) verwenden.
5. Hier ist ein Beispiel-Codeausschnitt:

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6. Um diese Funktion zu verwenden, definieren Sie die asynchrone Funktion und übergeben Sie sie als Parameter an die `promisify`-Funktion. Die zurückgegebene Funktion wird jetzt eine Promise zurückgeben.

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // Promise löst sich nach 2s auf
```

Die `delay`-Funktion ist ein Beispiel einer asynchronen Funktion, die jetzt eine Promise zurückgibt, indem sie die `promisify`-Funktion verwendet.
