# Using Logical AND with Functions

To start practicing coding, open the Terminal/SSH and type `node`.

To check if two functions return `true` for a given set of arguments, use the logical AND (`&&`) operator.

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

The above code creates a new function `both` that takes two functions `f` and `g` as input and returns another function that calls `f` and `g` with the supplied arguments and returns `true` only if both functions return `true`.

For example, to check if a number is both positive and even, we can use the `isEven` and `isPositive` functions with `both` as shown below:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

Here, `isPositiveEven` is a new function that checks if a given number is both positive and even by using the `both` function with `isEven` and `isPositive` as inputs.
