# Code Practice: Check if an Array is Sorted

To practice coding, open the Terminal/SSH and type `node`.

Here's a function to check if a numeric array is sorted:

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

To use it, pass an array of numbers to `isSorted()`. The function will return `1` if the array is sorted in ascending order, `-1` if it's sorted in descending order, and `0` if it's not sorted.

Here are some examples:

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
