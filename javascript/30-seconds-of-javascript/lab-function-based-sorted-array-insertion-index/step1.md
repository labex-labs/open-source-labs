# Function to Find Insertion Index in Sorted Array

To find the lowest index to insert a value in an array and maintain its sorting order, use the function `sortedIndexBy(arr, n, fn)` in JavaScript.

This function loosely checks if the array is sorted in descending order and then uses `Array.prototype.findIndex()` to find the appropriate index based on the iterator function `fn`.

Here's the code for the `sortedIndexBy()` function:

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

You can call the function with an array of objects, a value to insert, and an iterator function.

For example, `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` returns `0`, which is the index where the `{ x: 4 }` object should be inserted to maintain the sorting order based on the `x` property.
