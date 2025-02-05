# Check if a Number is Divisible

To check if a number is divisible by another number in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the modulo operator (`%`) to check if the remainder of the division is equal to `0`. If it is, then the number is divisible.

Here's an example function that checks if the first numeric argument is divisible by the second one:

```js
const isDivisible = (dividend, divisor) => dividend % divisor === 0;
```

You can test this function with `isDivisible(6, 3)`, which should return `true` since 6 is divisible by 3.
