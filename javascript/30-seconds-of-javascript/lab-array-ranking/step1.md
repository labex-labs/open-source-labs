# Ranking Arrays

To practice coding, open the Terminal/SSH and type `node`. This function calculates the ranking of an array based on a comparator function.

To use this function, you can:

- Use `Array.prototype.map()` and `Array.prototype.filter()` to map each element to a rank using the provided comparator function.

Here's an example usage:

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

Example:

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
