# Stable Sort

To perform stable sorting of an array and preserve the initial indexes of items with the same values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` to pair each element of the input array with its corresponding index.
3. Use `Array.prototype.sort()` along with a `compare` function to sort the list while preserving the initial order if the items compared are equal.
4. Use `Array.prototype.map()` again to convert the array items back to their initial form.
5. The original array is not mutated, and a new array is returned instead.

Here's an implementation of the `stableSort` function in JavaScript:

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

You can call the `stableSort` function with an array and a `compare` function to obtain a new array with the sorted items, as shown below:

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
