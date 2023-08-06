# How to Check if a Number Has Decimal Digits

To check if a number has any decimal digits, you can use the modulo operator in JavaScript. Follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the modulo (`%`) operator to check if the number is divisible by `1`.
3. If the result is not equal to zero, then the number has decimal digits.

Here's an example code to check if a number has decimal digits:

```js
const hasDecimals = (num) => num % 1 !== 0;
```

You can test the function by calling it with different numbers, like this:

```js
hasDecimals(1); // false
hasDecimals(1.001); // true
```
