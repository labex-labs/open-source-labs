# First N Elements

> To start practicing coding, open the Terminal/SSH and type `node`.

Gets the first `n` elements of an array.

- Use `Array.prototype.slice()` with a start value of `0` and an end value of `n` to get the first `n` elements of `arr`.

```js
const firstN = (arr, n) => arr.slice(0, n);
```

```js
firstN(['a', 'b', 'c', 'd'], 2); // ['a', 'b']
```
