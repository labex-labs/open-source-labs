# How to Ungroup Array Elements Based on a Function

If you need to ungroup elements in an array produced by `zip` and apply a function, you can use `unzipWith`. Here's how you can implement it:

1. Use `Math.max()` and the spread operator (`...`) to get the longest subarray in the array and `Array.prototype.map()` to make each element an array.
2. Use `Array.prototype.reduce()` and `Array.prototype.forEach()` to map grouped values to individual arrays.
3. Use `Array.prototype.map()` and the spread operator (`...`) to apply `fn` to each individual group of elements.

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

To use `unzipWith`, open the Terminal/SSH and type `node`. Then, you can run the following example:

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

This will create an array of elements by ungrouping the elements in the input array produced by `zip` and applying the provided function.
