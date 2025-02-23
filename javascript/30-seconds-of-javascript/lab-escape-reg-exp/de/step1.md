# Wie man in JavaScript reguläre Ausdrücke escapt

Um eine Zeichenfolge zu escapen, um sie in einem regulären Ausdruck in JavaScript zu verwenden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `String.prototype.replace()`, um Sonderzeichen zu escapen.
3. Kopieren und einfügen Sie den folgenden Codeausschnitt:

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. Verwenden Sie die `escapeRegExp()`-Funktion, um Sonderzeichen in einer Zeichenfolge zu escapen.

Hier ist ein Beispiel:

```js
escapeRegExp("(test)"); // \\(test\\)
```

Mit diesen Schritten können Sie nun leicht jedes Sonderzeichen in einem regulären Ausdruck in JavaScript escapen.
