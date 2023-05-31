# Check if a Stream is Readable

To check if a given argument is a readable stream, follow these steps:

- First, open the Terminal/SSH and type `node` to start practicing coding.
- Check if the value is not `null`.
- Use `typeof` to check if the value is an `object` and the `pipe` property is a `function`.
- Additionally, check if the `typeof` the `_read` and `_readableState` properties are `function` and `object`, respectively.

Here's an example function that implements these steps:

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

You can use this function to check if a stream is readable, like this:

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
