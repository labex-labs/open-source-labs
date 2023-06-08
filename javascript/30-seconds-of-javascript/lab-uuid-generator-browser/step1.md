# Generate UUID in Browser

To generate a UUID compliant with [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) version 4 in a browser, follow these steps:

1. Open the Terminal/SSH and type `node`.
2. Use the `Crypto.getRandomValues()` method to generate a UUID.
3. Convert the UUID to a hexadecimal string using the `Number.prototype.toString()` method.
4. Implement the following code:

```js
const crypto = require("crypto");
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. Call the `UUIDGeneratorBrowser()` function to generate a UUID. For example, `UUIDGeneratorBrowser()` would return `'7982fcfe-5721-4632-bede-6000885be57d'`.
