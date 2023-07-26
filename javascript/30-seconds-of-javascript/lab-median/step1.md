# How to Calculate the Median of an Array of Numbers

To calculate the median of an array of numbers, follow these steps:

1. Find the middle of the array.
2. Use `Array.prototype.sort()` to sort the values.
3. If `Array.prototype.length` is odd, return the number at the midpoint. If it is even, return the average of the two middle numbers.
4. To start practicing coding and using `node`, open the Terminal/SSH and type `node`.

Here's an example code snippet that implements this logic:

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

You can call this function with an array of numbers as shown below:

```js
median([5, 6, 50, 1, -5]); // 5
```
