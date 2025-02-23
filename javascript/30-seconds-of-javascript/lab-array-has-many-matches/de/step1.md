# Funktion zum Überprüfen, ob ein Array mehrere Übereinstimmungen hat

Um zu überprüfen, ob ein Array mehr als einen Wert hat, der einer angegebenen Funktion entspricht, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.filter()` in Kombination mit `fn`, um alle übereinstimmenden Array-Elemente zu finden.
3. Verwenden Sie `Array.prototype.length`, um zu überprüfen, ob mehr als ein Element `fn` entspricht.

Hier ist der Code, den Sie verwenden können:

```js
const hasMany = (arr, fn) => arr.filter(fn).length > 1;
```

Und hier sind einige Beispiele:

```js
hasMany([1, 3], (x) => x % 2); // true
hasMany([1, 2], (x) => x % 2); // false
```
