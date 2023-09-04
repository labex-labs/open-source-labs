# Partition Array Algorithm

To partition an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Apply the provided function `fn` to each value in the given array `arr`.
3. Split the array each time `fn` returns a new value.
4. Use `Array.prototype.reduce()` to create an accumulator object that holds the resulting array and the last value returned from `fn`.
5. Use `Array.prototype.push()` to add each value in `arr` to the appropriate partition in the accumulator array.
6. Return the resulting array.

Here is the code implementation:

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] },
  ).res;
```

Example usage:

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
