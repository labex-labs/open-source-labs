# Überprüfen, ob ein Stream beschreibbar ist

Um zu überprüfen, ob ein Stream beschreibbar ist, öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen. Dann folgen Sie diesen Schritten:

1. Überprüfen Sie, ob das übergebene Argument nicht `null` ist.
2. Verwenden Sie `typeof`, um zu überprüfen, ob der Wert ein `object` ist und ob die `pipe`-Eigenschaft eine `function` ist.
3. Überprüfen Sie zusätzlich, ob der `typeof` der `_write`- und `_writableState`-Eigenschaften jeweils `function` und `object` ist.

Hier ist ein Beispielcode, der diese Überprüfungen implementiert:

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Sie können diese Funktion mithilfe des `fs`-Moduls in Node.js testen. Beispiel:

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
