# Powerset

> To start practicing coding, open the Terminal/SSH and type `node`.

Returns the powerset of a given array of numbers.

- Use `Array.prototype.reduce()` combined with `Array.prototype.map()` to iterate over elements and combine into an array containing all combinations.

```js
const powerset = arr =>
  arr.reduce((a, v) => a.concat(a.map(r => r.concat(v))), [[]]);
```

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```
