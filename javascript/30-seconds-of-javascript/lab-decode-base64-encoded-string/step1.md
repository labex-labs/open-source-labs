# Decoding Base64 Encoded String

To decode a string of data that has been encoded using base-64 encoding, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a `Buffer` for the given string with base-64 encoding.
3. Use `Buffer.prototype.toString()` to return the decoded string.

Here's an example code snippet:

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

You can test this function by running `atob('Zm9vYmFy')` which should return `'foobar'`.
