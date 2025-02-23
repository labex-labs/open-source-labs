# Wie man in Node.js überprüft, ob ein Wert ein Stream ist

Um zu überprüfen, ob ein Wert in Node.js ein Stream ist, kannst du die `isStream`-Funktion verwenden. Um diese Funktion zu nutzen, folge diesen Schritten:

1. Öffne das Terminal/SSH.
2. Tippe `node`, um mit der Codeausführung zu beginnen.
3. Verwende die `isStream`-Funktion, um zu überprüfen, ob das gegebene Argument ein Stream ist.
4. Um zu überprüfen, ob der Wert von `null` verschieden ist, verwende folgenden Code:

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. Um zu überprüfen, ob eine Datei ein Stream ist, verwende folgenden Code:

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
