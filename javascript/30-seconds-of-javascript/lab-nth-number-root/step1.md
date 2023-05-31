# NTH Root of Number

> To start practicing coding, open the Terminal/SSH and type `node`.

Calculates the nth root of a given number.

- Use `Math.pow()` to calculate `x` to the power of `1 / n` which is equal to the nth root of `x`.

```js
const nthRoot = (x, n) => Math.pow(x, 1 / n);
```

```js
nthRoot(32, 5); // 2
```
