# How to Remove Array Elements From the End in JavaScript

To remove elements from the end of an array in JavaScript, you can use the `Array.prototype.slice()` method. Here's how you can do it:

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

This function creates a new array with the last `n` elements of the original array. Here's how you can use it:

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

To use this function, open the Terminal/SSH and type `node` to start practicing coding.
