# How to Find Array Similarity in JavaScript

To practice coding, open the Terminal/SSH and type `node`. This will help you understand how to find an array of elements that appear in both arrays. Follow these steps:

1. Use the `Array.prototype.includes()` method to determine the values that are not a part of `values`.
2. Use the `Array.prototype.filter()` method to remove them.

Here's the code to find the array similarity:

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

You can test this code by running the following command:

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

This will return `[1, 2]` as the output.
