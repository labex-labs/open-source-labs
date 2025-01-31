# How to Get Array Tail in JavaScript

To get all the elements in an array except for the first one, you can use the `Array.prototype.slice()` method. If the array length is more than 1, use `slice(1)` to return the array without the first element. Otherwise, return the whole array.

While negative slicing (like `slice(-4)`) is possible in JavaScript and slices from the end, we use `slice(1)` here because:

1. It clearly communicates our intent to skip the first element
2. It works consistently regardless of array length
3. Negative slicing would require knowing the array length to get the same result

Here's an example code:

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

You can now use the `tail()` function to get the array tail:

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
