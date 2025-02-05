# How to Find Insertion Index in Sorted Array

To find the lowest index at which a value should be inserted into a sorted array, follow these steps:

1. Check if the array is sorted in descending order.
2. Use `Array.prototype.findIndex()` method to find the appropriate index where the element should be inserted.

Here's the code to implement this:

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

You can call the `sortedIndex` function by passing the sorted array and the value you want to insert. Here are some examples:

```js
sortedIndex([5, 3, 2, 1], 4); // Output: 1
sortedIndex([30, 50], 40); // Output: 1
```

By using this function, you can easily find the insertion index of a value in a sorted array.
