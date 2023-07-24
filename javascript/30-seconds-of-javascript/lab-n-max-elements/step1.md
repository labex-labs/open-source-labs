# How to Get N Max Elements from an Array in JavaScript

To practice coding in JavaScript, open the Terminal/SSH and type `node`. Once you've done that, you can use the following steps to get the `n` maximum elements from an array:

1. Use `Array.prototype.sort()` along with the spread operator (`...`) to create a shallow clone of the array and sort it in descending order.
2. Use `Array.prototype.slice()` to get the specified number of elements.
3. If you omit the second argument, `n`, you will get a one-element array by default.
4. If `n` is greater than or equal to the provided array's length, then return the original array (sorted in descending order).

Here's the JavaScript code for the `maxN` function that implements these steps:

```js
const maxN = (arr, n = 1) => [...arr].sort((a, b) => b - a).slice(0, n);
```

You can test the `maxN` function with the following examples:

```js
maxN([1, 2, 3]); // [3]
maxN([1, 2, 3], 2); // [3, 2]
```
