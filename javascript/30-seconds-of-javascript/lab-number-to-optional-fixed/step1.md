# Number to Fixed-Point Notation Without Trailing Zeros

> To start practicing coding, open the Terminal/SSH and type `node`.

Formats a number using fixed-point notation, if it has decimals.

- Use `Number.prototype.toFixed()` to convert the number to a fixed-point notation string.
- Use `Number.parseFloat()` to convert the fixed-point notation string to a number, removing trailing zeros.
- Use a template literal to convert the number to a string.

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.500, 2); // '1.5'
```
