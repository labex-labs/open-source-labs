# How to Flatten an Array with JavaScript

To flatten an array up to a specified depth in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `flatten` function with two arguments: `arr` (the array to be flattened) and `depth` (the maximum number of nested levels to be flattened).
3. Inside the `flatten` function, use recursion to decrement `depth` by `1` for each level of depth.
4. Use `Array.prototype.reduce()` and `Array.prototype.concat()` to merge elements or arrays.
5. Add a base case for when `depth` is equal to `1` to stop the recursion.
6. Omit the second argument, `depth`, to flatten only to a depth of `1` (single flatten).

Here is the code for the `flatten` function:

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    [],
  );
```

You can test the `flatten` function with the following examples:

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
