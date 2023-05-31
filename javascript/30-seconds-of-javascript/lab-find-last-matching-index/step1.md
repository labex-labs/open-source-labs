# How to Find the Index of the Last Matching Element in an Array Using JavaScript

To find the index of the last element that matches a certain condition in a JavaScript array, use the `findLastIndex` function. Here's how to use it:

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

The `findLastIndex` function takes two arguments: the array to search and a function to test each element. Here's how it works:

1. Use `Array.prototype.map()` to create a new array of `[index, value]` pairs.
2. Use `Array.prototype.filter()` to remove elements from the array that don't match the condition provided by the `fn` function.
3. Use `Array.prototype.pop()` to get the last element in the filtered array.
4. If the filtered array is empty, return `-1`.

Here's an example of how to use `findLastIndex`:

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (index of the value 3)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (default value when not found)
```

To start practicing coding, open the Terminal/SSH and type `node`.
