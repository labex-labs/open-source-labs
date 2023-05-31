# How to Find the Maximum Value of an Array Based on a Function

To find the maximum value of an array based on a function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` to map each element of the array to the value returned by the provided function, `fn`.
3. Use `Math.max()` to get the maximum value of the mapped array.

Here's an example code snippet that implements the above steps:

```js
const maxBy = (arr, fn) =>
  Math.max(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

To use the `maxBy` function, pass in an array and the function that should be used to map each element to a value. You can either pass in a function directly or a string representing the key that should be used to access the value in each object of the array.

Here are some example calls to the `maxBy` function:

```js
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // returns 8
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // returns 8
```
