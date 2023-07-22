# How to Negate a Predicate Function in JavaScript

To negate a predicate function in JavaScript, you can use the `!` operator. To do this, you can create a higher-order function called `negate` that takes a predicate function and applies the `!` operator to it with its arguments. Here's an example of how to implement `negate`:

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

You can then use `negate` to negate any predicate function. Here's an example of how to use `negate` to filter out even numbers from an array:

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

In this example, `isEven` is a predicate function that checks if a number is even. We then use `negate` to create a new predicate function called `isOdd` that checks if a number is odd by negating `isEven`. Finally, we use `isOdd` with the `filter` method to filter out even numbers from the array.
