# Checking for Same Contents in Arrays

To check if two arrays contain the same elements regardless of order, follow these steps:

1. Open the Terminal/SSH and type `node`.
2. Use a `for...of` loop over a `Set` created from the values of both arrays.
3. Use `Array.prototype.filter()` to compare the amount of occurrences of each distinct value in both arrays.
4. Return `false` if the counts do not match for any element, `true` otherwise.

Here's the code for the same:

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

To test the function, use the following code:

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
