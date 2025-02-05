# Binary Search Algorithm

To begin coding practice, open the Terminal/SSH and type `node`. The binary search algorithm is used to find the index of a given element in a sorted array. Here are the steps to implement the binary search algorithm:

1. Declare the left and right search boundaries, `l` and `r`, initialized to `0` and the `length` of the array respectively.
2. Use a `while` loop to repeatedly narrow down the search subarray by dividing it in half using `Math.floor()`.
3. If the element is found, return its index. Otherwise, return `-1`.
4. Note that this algorithm does not account for duplicate values in the array.

Here's an example implementation of the binary search algorithm in JavaScript:

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

You can test the `binarySearch` function with the following examples:

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
