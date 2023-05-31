# Creating an Object from Key-Value Pairs

To create an object from key-value pairs, use the `objectFromPairs` function.

- Open the Terminal/SSH and type `node` to start practicing coding.
- The function uses `Array.prototype.reduce()` to create and combine key-value pairs.
- For a simpler implementation, you can also use [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries).

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

Example usage:

```js
objectFromPairs([
  ["a", 1],
  ["b", 2],
]); // {a: 1, b: 2}
```
