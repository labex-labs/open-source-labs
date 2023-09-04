# Generating UUID in Node.js

To generate a UUID in Node.js, follow the steps below:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `crypto.randomBytes()` method to generate a UUID that is compliant with [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) version 4.
3. Convert the generated UUID to a proper UUID (hexadecimal string) using the `Number.prototype.toString()` method.
4. Alternatively, you can use the [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) method that provides similar functionality.

Here's an example code snippet to generate UUID in Node.js:

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16),
  );
```

You can call the `UUIDGeneratorNode()` method to generate a UUID.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
