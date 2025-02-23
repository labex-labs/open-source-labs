# Eine Funktion zum Überprüfen, ob ein String mit einem Teilstring endet

Um zu überprüfen, ob ein gegebener String mit einem Teilstring eines anderen Strings endet, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie eine `for...in`-Schleife und `String.prototype.slice()`, um jeden Teilstring des gegebenen `word` von hinten beginnend zu erhalten.
3. Verwenden Sie `String.prototype.endsWith()`, um den aktuellen Teilstring mit dem `text` zu überprüfen.
4. Geben Sie den passenden Teilstring zurück, wenn er gefunden wird. Andernfalls geben Sie `undefined` zurück.

Hier ist der Codeausschnitt, um die obigen Schritte umzusetzen:

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

Sie können die Funktion mit dem folgenden Beispiel testen:

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
