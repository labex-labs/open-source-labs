# So führen Sie eine Funktion für jedes Array-Element in umgekehrter Reihenfolge aus

Um eine Funktion für jedes Array-Element, beginnend mit dem letzten Element des Arrays, auszuführen, folgen Sie diesen Schritten:

1. Klonen Sie das gegebene Array mit `Array.prototype.slice()`.
2. Kehren Sie das geklonte Array mit `Array.prototype.reverse()` um.
3. Verwenden Sie `Array.prototype.forEach()`, um über das umgekehrte Array zu iterieren.

Hier ist ein Beispielcodeausschnitt:

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

Sie können die Funktion testen, indem Sie folgenden Code ausführen:

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
