# Command-Line Arguments

To get the command-line arguments passed to a Node.js script, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `process.argv` to get an array of all command-line arguments.
3. Use `Array.prototype.slice()` to remove the first two elements, which are the path of the Node.js executable and the file being executed.

Here's an example code snippet that demonstrates how to get the command-line arguments using the `getCmdArgs` function:

```js
const getCmdArgs = () => process.argv.slice(2);

// Example usage: node my-script.js --name=John --age=30
getCmdArgs(); // ['--name=John', '--age=30']
```
