# How to Split an Array into Chunks of a Specific Size

To practice coding, open the Terminal/SSH and type `node`.

To split an array into smaller arrays of a specified size, follow these steps:

1. Use `Array.from()` to create a new array that fits the number of chunks that will be produced.
2. Use `Array.prototype.slice()` to map each element of the new array to a chunk the length of `size`.
3. If the original array cannot be split evenly, the final chunk will contain the remaining elements.

Here's an example code snippet:

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

You can use this function by passing in the array you want to split and the desired size of the chunks. For example:

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
