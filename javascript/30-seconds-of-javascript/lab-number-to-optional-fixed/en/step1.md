# Converting Numbers to Fixed-Point Notation

To convert a number to fixed-point notation without trailing zeros, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Number.prototype.toFixed()` to convert the number to a fixed-point notation string.
3. Use `Number.parseFloat()` to convert the fixed-point notation string back to a number, removing trailing zeros.
4. Use a template literal to convert the number to a string.

Example code:

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

You can test the function with different inputs:

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
