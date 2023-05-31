# Encode String to Base64

> To start practicing coding, open the Terminal/SSH and type `node`.

Creates a base-64 encoded ASCII string from a String object in which each character in the string is treated as a byte of binary data.

- Create a `Buffer` for the given string with binary encoding.
- Use `Buffer.prototype.toString()` to return the base-64 encoded string.

```js
const btoa = str => Buffer.from(str, 'binary').toString('base64');
```

```js
btoa('foobar'); // 'Zm9vYmFy'
```
