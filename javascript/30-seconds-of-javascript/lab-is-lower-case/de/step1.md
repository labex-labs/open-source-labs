# JavaScript-Funktion zum Überprüfen, ob ein String in Kleinbuchstaben geschrieben ist

Um zu überprüfen, ob ein gegebener String in Kleinbuchstaben geschrieben ist, können Sie die folgende JavaScript-Funktion verwenden. Zunächst wandeln Sie den String in Kleinbuchstaben um, indem Sie `String.prototype.toLowerCase()` verwenden, und vergleichen Sie ihn dann mit dem ursprünglichen String mithilfe von strikter Gleichheit (`===`).

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

Hier ist ein Beispiel für die Verwendung:

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

Um diese Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
