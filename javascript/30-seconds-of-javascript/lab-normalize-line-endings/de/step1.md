# Funktion zum Normalisieren von Zeilenenden

Um Zeilenenden in einer Zeichenfolge zu normalisieren, kannst du die folgende Funktion verwenden.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- Verwende `String.prototype.replace()` mit einem regulären Ausdruck, um Zeilenenden zu finden und durch die `normalized`-Version zu ersetzen.
- Standardmäßig ist die `normalized`-Version auf `'\r\n'` gesetzt.
- Um eine andere `normalized`-Version zu verwenden, übergebe sie als zweites Argument.

Hier sind einige Beispiele:

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
