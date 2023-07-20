# How to Digitize a Number

To digitize a number in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Math.abs()` to remove the sign of the number.
3. Convert the number to a string and use the spread operator (`...`) to create an array of digits.
4. Use `Array.prototype.map()` and `parseInt()` to convert each digit to an integer.

Here's the code for the `digitize` function:

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

Example usage:

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
