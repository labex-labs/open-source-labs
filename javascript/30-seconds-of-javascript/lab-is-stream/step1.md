# How to Check If a Value Is a Stream in Node.js

To check if a value is a stream in Node.js, you can use the `isStream` function. To use this function, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. Use the `isStream` function to check if the given argument is a stream.
4. To check if the value is different from `null`, use the following code:

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. To check if a file is a stream, use the following code:

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
