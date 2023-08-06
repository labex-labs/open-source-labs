# Check if a Value is an Async Function in JavaScript

To check if a value is an `async` function in JavaScript, you can use the following code:

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

This function uses `Object.prototype.toString()` and `Function.prototype.call()` to check whether the given argument is an `async` function.

You can test the function by passing a regular function and an `async` function as arguments:

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

To start practicing coding in JavaScript, open the Terminal/SSH and type `node`.
