# Wie man den Array-Endteil in JavaScript erhält

Um alle Elemente eines Arrays außer dem ersten zu erhalten, können Sie die `Array.prototype.slice()`-Methode verwenden. Wenn die Arraylänge größer als 1 ist, verwenden Sie `slice(1)`, um das Array ohne das erste Element zurückzugeben. Andernfalls geben Sie das gesamte Array zurück.

Während negative Slicing (wie `slice(-4)`) in JavaScript möglich ist und von der Endposition aus schneidet, verwenden wir hier `slice(1)`, weil:

1. Es kommuniziert eindeutig unseren Wunsch, das erste Element zu überspringen
2. Es funktioniert konsistent unabhängig von der Arraylänge
3. Negative Slicing würde zur gleichen Ergebnisgewinnung die Arraylänge kennen müssen

Hier ist ein Beispielcode:

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

Sie können jetzt die `tail()`-Funktion verwenden, um den Array-Endteil zu erhalten:

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
