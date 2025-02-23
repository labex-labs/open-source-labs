# Hier ist eine Funktion, um eine Zeichenkette umzukehren:

Um eine Zeichenkette umzukehren, verwenden Sie den Spread-Operator (`...`) und `Array.prototype.reverse()`. Verbinden Sie die Zeichen, um eine Zeichenkette zu erhalten, indem Sie `Array.prototype.join()` verwenden. Hier ist der Code:

```js
const reverseString = (str) => [...str].reverse().join("");
```

Beispielverwendung:

```js
reverseString("foobar"); // 'raboof'
```
