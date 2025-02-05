# Calculating the Factorial of a Number

To calculate the factorial of a number, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion to calculate the factorial.
3. If `n` is less than or equal to `1`, return `1`.
4. Otherwise, return the product of `n` and the factorial of `n - 1`.
5. If `n` is a negative number, throw a `TypeError`.

Here is the code to calculate the factorial:

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

You can test the code by calling the `factorial` function with a number as an argument:

```js
factorial(6); // 720
```
