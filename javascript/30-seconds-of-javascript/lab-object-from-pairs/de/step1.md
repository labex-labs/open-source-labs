# Ein Objekt aus Schlüssel-Wert-Paaren erstellen

Um ein Objekt aus Schlüssel-Wert-Paaren zu erstellen, verwenden Sie die `objectFromPairs`-Funktion.

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Die Funktion verwendet `Array.prototype.reduce()`, um Schlüssel-Wert-Paare zu erstellen und zu kombinieren.
- Für eine einfachere Implementierung können Sie auch [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries) verwenden.

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

Beispielverwendung:

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
