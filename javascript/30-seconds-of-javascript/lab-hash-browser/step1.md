# How to Calculate SHA-256 Hash in a Browser

To calculate the SHA-256 hash of a value in a browser, use the following code snippet:

```js
const hashBrowser = (val) => {
  return crypto.subtle
    .digest("SHA-256", new TextEncoder("utf-8").encode(val))
    .then((h) => {
      const hexes = [];
      const view = new DataView(h);
      for (let i = 0; i < view.byteLength; i += 4) {
        hexes.push(("00000000" + view.getUint32(i).toString(16)).slice(-8));
      }
      return hexes.join("");
    });
};
```

This function creates a hash for a value using the SHA-256 algorithm and returns a promise. To use it, pass the value to be hashed as an argument.

For example, to hash the following JSON object:

```js
{
  a: 'a',
  b: [1, 2, 3, 4],
  foo: { c: 'bar' }
}
```

Use the following code:

```js
hashBrowser(
  JSON.stringify({ a: "a", b: [1, 2, 3, 4], foo: { c: "bar" } })
).then(console.log);
```

This will output the following SHA-256 hash:

```
04aa106279f5977f59f9067fa9712afc4aedc6f5862a8defc34552d8c7206393
```
