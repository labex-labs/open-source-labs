# Finding the NTH Element of an Array

To find the nth element of an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.slice()` to create a new array containing the nth element.
3. If the index is out of bounds, return `undefined`.
4. Omit the second argument, `n`, to get the first element of the array.

Here's an example code that implements this:

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

You can test this function with the following examples:

```js
nthElement(["a", "b", "c"], 1); // Output: 'b'
nthElement(["a", "b", "b"], -3); // Output: 'a'
```

By following these steps, you can easily find the nth element of an array using JavaScript.
