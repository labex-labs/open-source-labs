# How to Calculate the Nth Root of a Number

To calculate the nth root of a number:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the formula `Math.pow(x, 1/n)` to calculate `x` to the power of `1/n`.
3. The result of this calculation is equal to the nth root of `x`.

Here's an example code snippet:

```js
const nthRoot = (x, n) => Math.pow(x, 1 / n);
nthRoot(32, 5); // Output: 2
```

This code will calculate the nth root of 32 (where n is 5) and return the output as 2.
