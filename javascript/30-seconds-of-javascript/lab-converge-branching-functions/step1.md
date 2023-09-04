# Converging Functions

To practice coding, open the Terminal/SSH and type `node`.

This function `converge` takes a converging function and a list of branching functions as input. It returns a new function that applies each branching function to the input arguments. The results of the branching functions are then passed as arguments to the converging function.

The `Array.prototype.map()` and `Function.prototype.apply()` methods are used to apply each function to the input arguments. The spread operator (`...`) is then used to call `converger` with the results of all other functions.

Here's the code for the `converge` function:

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

An example of how to use this function is shown below. The `average` function is created by calling `converge` with an anonymous function that calculates the average of an array. The branching functions are two anonymous functions that calculate the sum of an array and its length, respectively.

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length],
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

This code calculates the average of the array `[1, 2, 3, 4, 5, 6, 7]` and returns `4`.
