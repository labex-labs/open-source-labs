# Function to Calculate Sum of Mapped Array Elements

To calculate the sum of an array by mapping each element to a value using a provided function, use the `sumBy` function. This function uses `Array.prototype.map()` to map each element to the value returned by `fn`. It then uses `Array.prototype.reduce()` to add each value to an accumulator, which is initialized with a value of `0`.

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

Example Usage:

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // Returns 20
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // Returns 20
```

To start practicing coding with this function, open the Terminal/SSH and type `node`.
