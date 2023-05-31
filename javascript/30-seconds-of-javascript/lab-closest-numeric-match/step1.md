# A Function to Find the Closest Numeric Match in an Array

To find the closest number in an array, use the following function:

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

Here's how to use it:

1. Open the Terminal/SSH.
2. Type `node`.
3. Use the `closest()` function and provide the array and the target value as arguments.

Example usage: `closest([6, 1, 3, 7, 9], 5)` will return `6`, which is the closest number to `5` in the array.
