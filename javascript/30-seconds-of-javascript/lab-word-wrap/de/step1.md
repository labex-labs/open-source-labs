# Anweisungen zur Umbrücheiner Zeichenkette

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Dieser Code umbricht eine Zeichenkette auf eine gegebene Anzahl von Zeichen mit einem Zeilenumbruchzeichen. Um ihn zu verwenden, folgen Sie diesen Schritten:

1. Verwenden Sie `String.prototype.replace()` und eine reguläre Ausdruck, um ein angegebenes Umbruchzeichen an der nächsten Leerzeichenposition von `max` Zeichen einzufügen.
2. Wenn Sie nicht den Standardwert `'\n'` für das dritte Argument `br` verwenden möchten, können Sie es weglassen und Ihr eigenes Zeichen angeben.

Hier ist der Code:

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

Und hier sind einige Beispiele für die Verwendung:

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
