# How to Filter Out Matching Array Elements in JavaScript

To filter out elements in a JavaScript array that have one or more specified values, follow these steps:

1. Open the Terminal or SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.includes()` method to find the values to exclude.
3. Use the `Array.prototype.filter()` method to create a new array with the excluded elements.

Here is an example code snippet:

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

In this example, the `without` function takes an array `arr` and one or more arguments `args`. The function uses the `filter()` method to create a new array that excludes any elements that match any of the specified values in `args`. The `includes()` method is used to check if the value is in `args`. Finally, the function returns the new array with the excluded elements.
