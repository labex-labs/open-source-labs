# JavaScript Promises

Um zu überprüfen, ob ein Objekt promise-ähnlich ist, verwenden Sie die Funktion `isPromiseLike`. Diese Funktion überprüft, ob das Objekt nicht null ist, vom Typ object oder function ist und eine `.then`-Eigenschaft hat, die ebenfalls eine Funktion ist.

Hier ist der Code für `isPromiseLike`:

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

Hier sind einige Beispiele dafür, wie `isPromiseLike` verwendet werden kann:

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

Um zu beginnen, JavaScript zu programmieren, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
