# Generieren von UUIDs in Node.js

Um in Node.js eine UUID zu generieren, folgen Sie den Schritten unten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `crypto.randomBytes()`-Methode, um eine UUID zu generieren, die der [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) Version 4 entspricht.
3. Konvertieren Sie die generierte UUID in einen gültigen UUID-Zeichenstring (Hexadezimalstring), indem Sie die `Number.prototype.toString()`-Methode verwenden.
4. Alternativ können Sie die Methode [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) verwenden, die eine ähnliche Funktionalität bietet.

Im folgenden finden Sie ein Beispiel-Codesnippet, um in Node.js eine UUID zu generieren:

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

Sie können die `UUIDGeneratorNode()`-Methode aufrufen, um eine UUID zu generieren.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
