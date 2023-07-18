# Checking if a Value is a Generator Function

To check if a value is a generator function, you can use the `isGeneratorFunction` function. To begin practicing coding, open the Terminal/SSH and type `node`.

Here's how the `isGeneratorFunction` function works:

- It checks if the given argument is a generator function by using `Object.prototype.toString()` and `Function.prototype.call()`.
- If the result of the check is `'[object GeneratorFunction]'`, then the value is a generator function.

Here's the code for the `isGeneratorFunction` function:

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

And here are some examples of how to use it:

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
