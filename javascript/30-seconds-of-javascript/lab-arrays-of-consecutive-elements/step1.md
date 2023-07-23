# Finding Arrays of Consecutive Elements

To find arrays of consecutive elements, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.slice()` to create an array with `n - 1` elements removed from the start.
3. Use `Array.prototype.map()` and `Array.prototype.slice()` to map each element to an array of `n` consecutive elements.

Here's an example function that implements these steps:

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

You can call this function with an array and a number `n` to find all arrays of `n` consecutive elements in the array. For example:

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
