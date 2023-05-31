# How to Calculate the Greatest Common Divisor

To calculate the greatest common divisor between two or more numbers/arrays using code, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use the following code:

```js
const gcd = (...arr) => {
  const _gcd = (x, y) => (!y ? x : gcd(y, x % y));
  return [...arr].reduce((a, b) => _gcd(a, b));
};
```

3. The `gcd` function uses recursion.

4. The base case is when `y` equals `0`. In this case, the function returns `x`.

5. Otherwise, the function returns the GCD of `y` and the remainder of the division `x / y`.

6. To test the function, use the following code:

```js
gcd(8, 36); // 4
gcd(...[12, 8, 32]); // 4
```
