# Function to Map Consecutive Elements in an Array

To start coding, open the Terminal/SSH and type `node`.

This function maps each block of `n` consecutive elements in an array, using the given function `fn`. Follow these steps:

- Use `Array.prototype.slice()` to obtain a new array `arr` with the first `n` elements removed.
- Use `Array.prototype.map()` and `Array.prototype.slice()` to apply `fn` to each block of `n` consecutive elements in `arr`.

Here's the code:

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

For example, you can use `mapConsecutive()` to map each block of 3 consecutive elements in an array of numbers, joining them with dashes:

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
