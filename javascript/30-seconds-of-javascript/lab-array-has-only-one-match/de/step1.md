# Funktion zum Überprüfen, ob ein Array nur einen Treffer hat

Um zu überprüfen, ob ein Array nur einen Wert hat, der der angegebenen Funktion entspricht, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.filter()` in Kombination mit `fn`, um alle passenden Arrayelemente zu finden.
3. Verwenden Sie `Array.prototype.length`, um zu überprüfen, ob nur ein Element `fn` entspricht.

Hier ist der Code:

```js
const hasOne = (arr, fn) => arr.filter(fn).length === 1;
```

Und hier ist ein Beispiel:

```js
hasOne([1, 2], (x) => x % 2); // true
hasOne([1, 3], (x) => x % 2); // false
```
