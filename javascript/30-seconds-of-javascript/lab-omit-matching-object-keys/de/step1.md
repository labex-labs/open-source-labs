# Entfernen von Objekt-Schlüsseln basierend auf einer Callback-Funktion

Um Objekt-Schlüssel basierend auf einer Callback-Funktion zu entfernen, verwenden Sie die `omitBy`-Funktion.

- `omitBy` erstellt ein Objekt, das aus den Eigenschaften besteht, für die die gegebene Funktion `falsy` zurückgibt.
- `Object.keys()` und `Array.prototype.filter()` werden verwendet, um die Schlüssel zu entfernen, für die `fn` einen `truthy`-Wert zurückgibt.
- `Array.prototype.reduce()` wandelt die gefilterten Schlüssel wieder in ein Objekt mit den entsprechenden Schlüssel-Wert-Paaren um.
- Die Callback-Funktion nimmt zwei Argumente entgegen: `value` und `key`.
- Im folgenden Beispiel wird gezeigt, wie `omitBy` verwendet wird, um numerische Schlüssel aus einem Objekt zu entfernen.

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
