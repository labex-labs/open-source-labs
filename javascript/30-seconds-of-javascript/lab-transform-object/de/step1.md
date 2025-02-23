# Objekttransformation

Um zu beginnen, das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `transform`-Funktion wendet eine bestimmte Funktion auf einen Akkumulator und jede Schlüssel im Objekt von links nach rechts an. So können Sie sie verwenden:

- Verwenden Sie `Object.keys()`, um über jede Schlüssel im Objekt zu iterieren.
- Verwenden Sie `Array.prototype.reduce()`, um die angegebene Funktion auf den angegebenen Akkumulator anzuwenden.

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

Hier ist ein Beispiel:

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
