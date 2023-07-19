# Consecutive Element Subarrays

To practice coding, open the Terminal/SSH and type `node`. The following code creates an array of `n`-tuples of consecutive elements.

```js
const aperture = (n, arr) =>
  n > arr.length ? [] : arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

To use the function:

- Call `aperture(n, arr)` function with `n` as the number of consecutive elements and `arr` as the array of numbers.
- The function returns an array of `n`-tuples of consecutive elements from `arr`.
- If `n` is greater than the length of `arr`, the function returns an empty array.

Example usage:

```js
aperture(2, [1, 2, 3, 4]); // [[1, 2], [2, 3], [3, 4]]
aperture(3, [1, 2, 3, 4]); // [[1, 2, 3], [2, 3, 4]]
aperture(5, [1, 2, 3, 4]); // []
```
