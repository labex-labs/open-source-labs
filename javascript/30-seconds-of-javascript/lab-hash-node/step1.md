# How to Calculate SHA-256 Hash in Node.js

To calculate a hash using the SHA-256 algorithm in Node.js, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `crypto.createHash()` method to create a `Hash` object with the appropriate algorithm.
3. Add the data from `val` to the `Hash` object using the `hash.update()` method.
4. Calculate the digest of the data using the `hash.digest()` method.
5. To prevent blocking on a long operation, use the `setTimeout()` method.
6. Return a `Promise` to give it a familiar interface.

Here's the code to calculate SHA-256 hash in Node.js:

```js
const crypto = require("crypto");

const hashNode = (val) =>
  new Promise((resolve) =>
    setTimeout(
      () => resolve(crypto.createHash("sha256").update(val).digest("hex")),
      0
    )
  );
```

To use the `hashNode()` function, pass the data as a parameter and call the `then()` method with a `console.log()` statement to print the hash to the console:

```js
hashNode(JSON.stringify({ a: "a", b: [1, 2, 3, 4], foo: { c: "bar" } })).then(
  console.log
);
// '04aa106279f5977f59f9067fa9712afc4aedc6f5862a8defc34552d8c7206393'
```
