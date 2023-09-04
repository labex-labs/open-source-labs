# How to Split an Array into N Chunks

To split an array into `n` smaller arrays, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Math.ceil()` and `Array.prototype.length` to calculate the size of each chunk.
3. Use `Array.from()` to create a new array of size `n`.
4. Use `Array.prototype.slice()` to map each element of the new array to a chunk the length of `size`.
5. If the original array cannot be split evenly, the final chunk will contain the remaining elements.

Here is an example implementation of the `chunkIntoN` function in JavaScript:

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size),
  );
};
```

You can use this function to split an array into `n` chunks by passing the array and the desired number of chunks as arguments. For example:

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
