# Checking if a Stream is Duplex

To check if a stream is duplex (readable and writable), open the Terminal/SSH and type `node` to start practicing coding. Then, follow these steps:

1. Check if the given argument is different from `null`.
2. Use `typeof` to check if the given argument is of type `object` and if it has a `pipe` property of type `function`.
3. Additionally, check if the `_read`, `_write`, `_readableState`, and `_writableState` properties are of type `function` and `object`, respectively.

Here's the code:

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

You can test this code using the following example:

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
