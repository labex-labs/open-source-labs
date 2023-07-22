# How to Ungroup Array Elements in JavaScript

To ungroup the elements in an array produced by the `zip` function, you can create an array of arrays using the `unzip` function in JavaScript. Here's how:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Math.max()`, `Function.prototype.apply()` to get the longest subarray in the array, and `Array.prototype.map()` to make each element an array.
3. Use `Array.prototype.reduce()` and `Array.prototype.forEach()` to map grouped values to individual arrays.

Here's the code for the `unzip` function:

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length)),
    }).map((x) => [])
  );
```

You can use the `unzip` function with the following examples:

```js
unzip([
  ["a", 1, true],
  ["b", 2, false],
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2],
]); // [['a', 'b'], [1, 2], [true]]
```

By following these steps, you can easily ungroup array elements in JavaScript.
