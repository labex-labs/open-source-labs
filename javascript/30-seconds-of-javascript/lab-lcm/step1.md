# Calculating Least Common Multiple

To calculate the least common multiple of two or more numbers, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the greatest common divisor (GCD) formula and the fact that `lcm(x, y) = x * y / gcd(x, y)` to determine the least common multiple.
3. The GCD formula uses recursion.
4. Implement the following code in JavaScript:

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

Example usage:

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
