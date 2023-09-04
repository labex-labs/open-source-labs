# Check if Process Arguments Contain Flags

To check if the current process's arguments contain specified flags, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.every()` and `Array.prototype.includes()` to check if `process.argv` contains all the specified flags.
3. Use a regular expression to test if the specified flags are prefixed with `-` or `--` and prefix them accordingly.

Here's a code snippet that shows how to implement this:

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag),
  );
```

You can test the function with different flags like this:

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
