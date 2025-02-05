# Encoding a String to Base64

To encode a String object to a base-64 encoded ASCII string, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding.
2. Create a `Buffer` using the given string and the binary encoding.
3. Use `Buffer.prototype.toString()` to return the base-64 encoded string.

Here's an example code snippet:

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

You can now use the `encodeToBase64()` function to encode any string to base-64. For example:

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
