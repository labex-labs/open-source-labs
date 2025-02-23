# Überprüfen, ob ein Stream duplex ist

Um zu überprüfen, ob ein Stream duplex (lesbar und beschreibbar) ist, öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen. Anschließend folgen Sie diesen Schritten:

1. Überprüfen Sie, ob das gegebene Argument von `null` unterschiedlich ist.
2. Verwenden Sie `typeof`, um zu überprüfen, ob das gegebene Argument vom Typ `object` ist und ob es eine `pipe`-Eigenschaft vom Typ `function` hat.
3. Überprüfen Sie außerdem, ob die `_read`, `_write`, `_readableState` und `_writableState`-Eigenschaften vom Typ `function` bzw. `object` sind.

Hier ist der Code:

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Sie können diesen Code mit dem folgenden Beispiel testen:

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
