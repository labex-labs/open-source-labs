# Funktion, um zu überprüfen, ob ein String mit einem Teilstring beginnt

Um zu überprüfen, ob ein gegebener String mit einem Teilstring eines anderen Strings beginnt, folgen Sie den Schritten unten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Verwenden Sie eine `for...in`-Schleife und die `String.prototype.slice()`-Methode, um jeden Teilstring des gegebenen `word` zu erhalten, beginnend am Anfang.
- Verwenden Sie die `String.prototype.startsWith()`-Methode, um den aktuellen Teilstring mit dem `text` zu überprüfen.
- Wenn ein übereinstimmender Teilstring gefunden wird, geben Sie ihn zurück. Andernfalls geben Sie `undefined` zurück.

Hier ist eine JavaScript-Funktion, die dies tut:

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

Sie können diese Funktion wie folgt aufrufen:

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // gibt '/>' zurück
```
