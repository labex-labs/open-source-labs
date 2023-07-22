# Binomial Coefficient Calculation

To calculate the number of ways to choose `k` items from `n` items without repetition and without order, you can use the following JavaScript function:

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

To use the function, open the Terminal/SSH and type `node`. Then, call the function with the desired values. For example:

```js
binomialCoefficient(8, 2); // 28
```

To ensure the function works correctly, you can follow these steps:

1. Use `Number.isNaN()` to check if any of the two values is `NaN`.
2. Check if `k` is less than `0`, greater than or equal to `n`, equal to `1` or `n - 1` and return the appropriate result.
3. Check if `n - k` is less than `k` and switch their values accordingly.
4. Loop from `2` through `k` and calculate the binomial coefficient.
5. Use `Math.round()` to account for rounding errors in the calculation.
