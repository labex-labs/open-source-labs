# How to Initialize an N-Dimensional Array in JavaScript

To create an N-dimensional array in JavaScript, you can use the `initializeNDArray` function. This function takes a value and any number of dimensions as arguments and returns a new array initialized with that value.

To use `initializeNDArray`, you can follow these steps:

1. Open the Terminal/SSH and type `node` to start coding.
2. Use recursion to create the array with the given number of dimensions.
3. Use `Array.from()` and `Array.prototype.map()` to generate rows where each row is a new array initialized using `initializeNDArray()`.

Here's the code for the `initializeNDArray` function:

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

You can then call `initializeNDArray` with the desired value and number of dimensions. For example:

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
