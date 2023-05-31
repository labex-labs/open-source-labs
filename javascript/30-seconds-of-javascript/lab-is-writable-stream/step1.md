# Checking if a Stream is Writable

To check if a stream is writable, open the Terminal/SSH and type `node` to start practicing coding. Then, follow these steps:

1. Check if the given argument is not `null`.
2. Use `typeof` to check if the value is an `object` and if the `pipe` property is a `function`.
3. Additionally, check if the `typeof` the `_write` and `_writableState` properties are `function` and `object`, respectively.

Here's an example code that implements these checks:

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

You can test this function using the `fs` module in Node.js. For example:

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
