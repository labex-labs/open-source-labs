# Code Practice: Quotient and Module of Division

To practice coding, open the Terminal/SSH and type `node`. This code returns an array that consists of the quotient and remainder of the given numbers.

To get the quotient of the division `x / y`, use `Math.floor()`. To get the remainder of the division `x / y`, use the modulo operator (`%`).

```js
const divmod = (x, y) => [Math.floor(x / y), x % y];
```

For example:

```js
divmod(8, 3); // [2, 2]
divmod(3, 8); // [0, 3]
divmod(5, 5); // [1, 0]
```
