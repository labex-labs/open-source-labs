# Ein String in Kebab Case umwandeln

Um einen String in Kebab Case umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Verwenden Sie `String.prototype.match()`, um den String mit einem geeigneten regulären Ausdruck in Wörter aufzuteilen.
3. Verwenden Sie `Array.prototype.map()`, `Array.prototype.join()` und `String.prototype.toLowerCase()`, um die Wörter zu kombinieren und `-` als Separator hinzuzufügen.

Hier ist eine Beispiel-Funktion, die die Umwandlung durchführt:

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

Sie können diese Funktion verwenden, um Strings in Kebab Case umzuwandeln, wie im folgenden gezeigt:

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); // 'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
