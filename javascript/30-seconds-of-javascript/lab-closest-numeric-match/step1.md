# Closest Numeric Match

> To start practicing coding, open the Terminal/SSH and type `node`.

Finds the closest number from an array.

- Use `Array.prototype.reduce()` to scan all elements of the array.
- Use `Math.abs()` to compare each element's distance from the target value, storing the closest match.

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

```js
closest([6, 1, 3, 7, 9], 5); // 6
```
