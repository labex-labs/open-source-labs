# How to remove array elements in JavaScript

To remove elements from the beginning of an array in JavaScript, follow these steps:

1. Open the Terminal or SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.slice()` method to create a new array with `n` elements removed from the beginning.
3. Use the `take` function in the code snippet below to implement the logic.

```js
const take = (arr, n = 1) => arr.slice(0, n);
```

Here's an example of how to use the `take` function:

```js
take([1, 2, 3], 5); // [1, 2, 3]
take([1, 2, 3], 0); // []
```

In the first example, `take([1, 2, 3], 5)` returns `[1, 2, 3]` because there are only 3 elements in the array. In the second example, `take([1, 2, 3], 0)` returns `[]` because no elements are taken from the beginning of the array.
