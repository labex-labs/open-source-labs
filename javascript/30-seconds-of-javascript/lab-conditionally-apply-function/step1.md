# Using When Function to Apply Condition

To apply a function when a certain condition is met, use the `when` function. To start, open the Terminal/SSH and type `node`.

The `when` function returns a new function that takes one argument and runs a callback if the argument is truthy, or returns the argument if it is falsy. The function expects a single value, `x`, and returns the appropriate value based on the `pred` parameter.

Here's an example implementation of the `when` function:

```js
const when = (pred, whenTrue) => (x) => pred(x) ? whenTrue(x) : x;
```

You can use the `when` function to create a new function that doubles even numbers:

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
