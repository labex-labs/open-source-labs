# Überprüfen, ob ein Stream lesbar ist

Um zu überprüfen, ob ein gegebener Argument ein lesbarer Stream ist, folgen Sie diesen Schritten:

- Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Überprüfen Sie, ob der Wert nicht `null` ist.
- Verwenden Sie `typeof`, um zu überprüfen, ob der Wert ein `object` ist und die `pipe`-Eigenschaft eine `function` ist.
- Überprüfen Sie zusätzlich, ob der `typeof` der `_read`- und `_readableState`-Eigenschaften jeweils `function` und `object` ist.

Hier ist eine Beispielfunktion, die diese Schritte implementiert:

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

Sie können diese Funktion verwenden, um zu überprüfen, ob ein Stream lesbar ist, wie folgt:

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
