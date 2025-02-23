# Funktion, um zu überprüfen, ob ein Wert vom Typ ist

Um zu überprüfen, ob ein bereitgestellter Wert vom angegebenen Typ ist, führen Sie die folgenden Schritte aus:

- Stellen Sie sicher, dass der Wert nicht `undefined` oder `null` ist, indem Sie `Array.prototype.includes()` verwenden.
- Verwenden Sie `Object.prototype.constructor`, um die `constructor`-Eigenschaft des Werts mit dem angegebenen `type` zu vergleichen.
- Die unten stehende Funktion `is()` führt diese Überprüfungen durch und gibt `true` zurück, wenn der Wert vom angegebenen Typ ist, und `false` andernfalls.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

Sie können `is()` verwenden, um zu überprüfen, ob ein Wert von verschiedenen Typen ist, wie `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number` und `Boolean`. Beispielsweise:

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
