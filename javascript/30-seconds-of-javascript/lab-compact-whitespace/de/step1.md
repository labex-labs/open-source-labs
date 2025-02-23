# Funktion zum Zusammenfassen von Leerzeichen in einer Zeichenkette

Um Leerzeichen in einer Zeichenkette zusammenzufassen, verwenden Sie die `compactWhitespace()`-Funktion.

- Sie verwendet `String.prototype.replace()` mit einem regulären Ausdrucksmuster, um alle Vorkommen von 2 oder mehr Leerzeichen durch ein einzelnes Leerzeichen zu ersetzen.
- Die Funktion nimmt eine Zeichenkette als Argument entgegen und gibt die zusammengefasste Zeichenkette zurück.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

Beispielverwendung:

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
