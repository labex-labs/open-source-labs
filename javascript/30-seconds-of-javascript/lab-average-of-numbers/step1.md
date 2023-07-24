# How to Calculate the Average of Numbers in JavaScript

To calculate the average of two or more numbers in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the built-in `Array.prototype.reduce()` method to add each value to an accumulator, initialized with a value of `0`.
3. Divide the resulting sum by the length of the array.

Here's an example code snippet you can use:

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

You can call the `average` function with an array or multiple arguments:

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
