# Decode Base64 Encoded String

> To start practicing coding, open the Terminal/SSH and type `node`.

Decodes a string of data which has been encoded using base-64 encoding.

- Create a `Buffer` for the given string with base-64 encoding.
- Use `Buffer.prototype.toString()` to return the decoded string.

```js
const atob = str => Buffer.from(str, 'base64').toString('binary');
```

```js
atob('Zm9vYmFy'); // 'foobar'
```
