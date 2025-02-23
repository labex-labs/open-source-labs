# Case-insensitive Substring-Suche

Um zu überprüfen, ob eine Zeichenfolge einen Substring enthält, unabhängig von der Groß-/Kleinschreibung, folgen Sie diesen Schritten:

- Verwenden Sie den `RegExp`-Konstruktor mit dem `'i'-Flag`, um eine reguläre Ausdruck zu erstellen, der die gegebene `searchString` ignorierend die Groß-/Kleinschreibung abgleicht.
- Verwenden Sie `RegExp.prototype.test()`, um zu überprüfen, ob die Zeichenfolge den Substring enthält.

Hier ist ein Beispielcodeausschnitt:

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

Um diese Funktion zu testen, können Sie ausführen:

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
