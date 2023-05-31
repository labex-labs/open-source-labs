# Instructions for Calculating the Average of a Mapped Array

To calculate the average of an array, you can map each element to a new value using the provided function. Here are the steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` to map each element to the value returned by `fn`.
3. Use `Array.prototype.reduce()` to add each mapped value to an accumulator, initialized with a value of `0`.
4. Divide the resulting array by its length to get the average.

Here's the code you can use:

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

You can test this function using the following examples:

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
