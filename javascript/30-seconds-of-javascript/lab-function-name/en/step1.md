# How to Get the Name of a Function in JavaScript

To get the name of a JavaScript function, follow these steps:

1. Open the Terminal or SSH.
2. Type `node` to start practicing coding.
3. Use `console.debug()` and the `name` property of the passed function to log the function's name to the `debug` channel of the console.
4. Return the given function `fn`.

Here's an example code snippet that demonstrates how to get the name of a function in JavaScript:

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// The function name 'max' is logged in the debug channel of the console.
// m = 6
```

In this example, the `functionName` function logs the name of the passed function to the console's `debug` channel and returns the function itself. The `name` property of the function is used to get its name.
