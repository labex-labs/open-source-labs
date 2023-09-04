# Calculating Percentile of Matches

To calculate the percentile of matches in the given array below or equal to a given value, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding practice.
2. Use the `Array.prototype.reduce()` method to calculate the number of values below the given value and the number of values equal to the given value.
3. Apply the percentile formula to obtain the percentage of matches.
4. Here's an example code snippet:

```js
const percentile = (arr, val) =>
  (100 *
    arr.reduce(
      (acc, v) => acc + (v < val ? 1 : 0) + (v === val ? 0.5 : 0),
      0,
    )) /
  arr.length;
```

5. To test the function, use this example code:

```js
percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6); // Output: 55
```

This function will output the percentage of matches in the given array that are less than or equal to the given value.
