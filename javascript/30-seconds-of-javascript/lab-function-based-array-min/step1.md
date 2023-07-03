# Function to Return Minimum Value of an Array

To start practicing coding, open the Terminal/SSH and type `node`.

This function returns the minimum value of an array, based on the provided function.

To do this, it uses `Array.prototype.map()` to map each element to the value returned by the function. It then uses `Math.min()` to get the minimum value.

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

You can use this function by passing an array and a function. For example:

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
