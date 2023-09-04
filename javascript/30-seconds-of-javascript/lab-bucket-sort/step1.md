# Bucket Sort Algorithm

To use the bucket sort algorithm and sort an array of numbers, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Find the minimum and maximum values of the given array using `Math.min()`, `Math.max()` and the spread operator (`...`).
3. Create the appropriate number of `buckets` (empty arrays) using `Array.from()` and `Math.floor()`.
4. Populate each bucket with the appropriate elements from the array using `Array.prototype.forEach()`.
5. Sort each bucket and append it to the result using `Array.prototype.reduce()`, the spread operator (`...`) and `Array.prototype.sort()`.

Here is an example implementation of the bucket sort algorithm in JavaScript:

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => [],
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

To test the algorithm, run the following code:

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
