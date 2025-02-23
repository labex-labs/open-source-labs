# Umwandeln eines Objekts in Paare

Um ein Objekt in ein Array von Schlüssel-Wert-Paaren umzuwandeln, verwenden Sie die `toPairs`-Funktion. Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `toPairs`-Funktion funktioniert wie folgt:

- Zunächst überprüft sie, ob `Symbol.iterator` für das gegebene iterierbare Objekt definiert ist.
- Wenn `Symbol.iterator` definiert ist, verwendet sie `Array.prototype.entries()`, um einen Iterator für das Objekt zu erhalten, und wandelt das Ergebnis anschließend mit `Array.from()` in ein Array von Schlüssel-Wert-Paar-Arrays um.
- Wenn `Symbol.iterator` für das Objekt nicht definiert ist, verwendet sie stattdessen `Object.entries()`.

Hier ist der Code für die `toPairs`-Funktion:

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

Sie können die `toPairs`-Funktion mit verschiedenen Objekttypen verwenden, wie z.B.:

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0','s'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
