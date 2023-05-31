# How to Read File Lines in Node.js

To read file lines in Node.js, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `fs.readFileSync()` to create a `Buffer` from the file you want to read.
3. Use `Buffer.prototype.toString()` to convert the buffer to a string.
4. Use `String.prototype.split()` to create an array of lines from the file's contents.
5. Call the `readFileLines` function with the file name as its argument.

Here's an example code snippet:

```js
const fs = require("fs");

const readFileLines = (filename) => {
  const buffer = fs.readFileSync(filename);
  return buffer.toString("UTF8").split("\n");
};

// Example usage
const arr = readFileLines("test.txt");
console.log(arr); // ['line1', 'line2', 'line3']
```

In the example above, `readFileLines` is a function that takes a filename as its argument and returns an array of lines from the file. The `fs.readFileSync()` method reads the file synchronously and returns a buffer. We then convert this buffer to a string using `Buffer.prototype.toString()`. Finally, we split the string into an array of lines using `String.prototype.split()`.
