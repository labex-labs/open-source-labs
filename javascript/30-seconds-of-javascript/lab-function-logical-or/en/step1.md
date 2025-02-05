# Using Logical Or for Functions

To start practicing coding, open the Terminal/SSH and type `node`.

The logical or (`||`) operator can be used to check if at least one function returns `true` for a given set of arguments. To do this, call the two functions with the supplied `args` and apply the logical or operator on their results.

Here's an example implementation of `either` function:

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

And here's an example usage of `either` function with two functions `isEven` and `isPositive`:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

In this example, `isPositiveOrEven` returns `true` for both `4` and `3` because `isEven` returns `true` for `4` and `isPositive` returns `true` for `3`.
