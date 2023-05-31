# Number Has Decimal Digits

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if a number has any decimals digits

- Use the modulo (`%`) operator to check if the number is divisible by `1` and return the result.

```js
const hasDecimals = num => num % 1 !== 0;
```

```js
hasDecimals(1); // false
hasDecimals(1.001); // true
```
