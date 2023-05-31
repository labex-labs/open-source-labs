# Filter Out Matching Array Elements

> To start practicing coding, open the Terminal/SSH and type `node`.

Filters out the elements of an array that have one of the specified values.

- Use `Array.prototype.includes()` to find values to exclude.
- Use `Array.prototype.filter()` to create an array excluding them.

```js
const without = (arr, ...args) => arr.filter(v => !args.includes(v));
```

```js
without([2, 1, 2, 3], 1, 2); // [3]
```
