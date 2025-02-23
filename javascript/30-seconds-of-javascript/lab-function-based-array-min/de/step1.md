# Funktion zum Zurückgeben des kleinsten Werts eines Arrays

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion gibt den kleinsten Wert eines Arrays zurück, basierend auf der bereitgestellten Funktion.

Dazu verwendet sie `Array.prototype.map()`, um jedes Element auf den von der Funktion zurückgegebenen Wert abzubilden. Anschließend verwendet sie `Math.min()`, um den kleinsten Wert zu erhalten.

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Sie können diese Funktion verwenden, indem Sie ein Array und eine Funktion übergeben. Beispielsweise:

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
