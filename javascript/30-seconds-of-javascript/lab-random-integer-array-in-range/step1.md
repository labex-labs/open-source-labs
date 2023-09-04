# Generating a Random Integer Array in a Specific Range

To generate an array of random integers within a specific range, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.from()` to create an empty array of the desired length.
3. Use `Math.random()` to generate random numbers and map them to the specified range. Use `Math.floor()` to convert them into integers.
4. The function `randomIntArrayInRange()` takes three arguments: `min`, `max`, and an optional argument `n` (default value is 1).
5. Call the `randomIntArrayInRange()` function with the desired `min`, `max`, and `n` values to generate the random integer array.

Here's the code:

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min,
  );
```

Example usage:

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
