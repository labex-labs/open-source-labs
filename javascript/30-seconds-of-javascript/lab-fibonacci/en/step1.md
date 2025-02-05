# Fibonacci Sequence

To generate the Fibonacci sequence in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node`.
2. Use `Array.from()` to create an empty array of the specific length, initializing the first two values (`0` and `1`).
3. Use `Array.prototype.reduce()` and `Array.prototype.concat()` to add values into the array, using the sum of the last two values, except for the first two.
4. Call the `fibonacci()` function and pass the desired length of the sequence as an argument.

Here's the code:

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

This will generate an array containing the Fibonacci sequence up until the nth term.
