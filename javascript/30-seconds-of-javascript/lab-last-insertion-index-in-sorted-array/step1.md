# Description of Last Insertion Index in Sorted Array

To find the highest index where a value should be inserted into an array in order to maintain its sort order, follow these steps:

- First, loosely check if the array is sorted in descending order.
- Then, use `Array.prototype.reverse()` and `Array.prototype.findIndex()` to find the appropriate last index where the element should be inserted.

Here is the code for the function:

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

And here is an example of how to use the function:

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

To start practicing coding, open the Terminal/SSH and type `node`.
