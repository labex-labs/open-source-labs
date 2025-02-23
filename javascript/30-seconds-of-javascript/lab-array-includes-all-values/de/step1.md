# Funktion zum Überprüfen, ob ein Array alle Werte enthält

Wenn Sie überprüfen möchten, ob alle Elemente eines Arrays `values` in einem anderen Array `arr` enthalten sind, können Sie die `includesAll`-Funktion in JavaScript verwenden.

Um die Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

So funktioniert die `includesAll`-Funktion:

- Sie verwendet die Methoden `Array.prototype.every()` und `Array.prototype.includes()`, um zu überprüfen, ob alle Elemente in `values` in `arr` enthalten sind.
- Wenn alle Elemente in `values` in `arr` enthalten sind, wird die Funktion `true` zurückgeben. Andernfalls wird `false` zurückgegeben.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

Hier ist ein Beispiel dafür, wie die `includesAll`-Funktion verwendet werden kann:

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
