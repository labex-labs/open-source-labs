# All Matches Index

To find all indexes of `val` in an array, use `Array.prototype.reduce()` to loop over the elements and store the indexes for matching elements. If `val` never occurs, an empty array is returned.

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

Example usage:

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

To start practicing coding, open the Terminal/SSH and type `node`.

This is an index of all matches.
