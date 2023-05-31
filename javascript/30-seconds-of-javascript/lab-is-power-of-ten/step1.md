# Check If a Number Is a Power of Ten

To check if a number is a power of ten, open the Terminal/SSH and type `node`.

Here's the code you can use to determine if `n` is a power of `10`:

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

Use `isPowerOfTen()` function to determine whether a given number is a power of ten.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
