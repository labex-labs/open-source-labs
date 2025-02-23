# Ein Zahl umkehren

Um eine Zahl in JavaScript umzukehren, können Sie die Funktion `reverseNumber()` mit den folgenden Schritten verwenden:

1. Konvertieren Sie die Zahl `n` in einen String, indem Sie `Object.prototype.toString()` verwenden.
2. Verwenden Sie `String.prototype.split()`, `Array.prototype.reverse()` und `Array.prototype.join()`, um den umgekehrten Wert von `n` als String zu erhalten.
3. Konvertieren Sie den String wieder in eine Zahl, indem Sie `parseFloat()` verwenden.
4. Behalten Sie das Vorzeichen der Zahl bei, indem Sie `Math.sign()` verwenden.

Hier ist der Code für die Funktion `reverseNumber()`:

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

Sie können die Funktion mit diesen Beispielen testen:

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
