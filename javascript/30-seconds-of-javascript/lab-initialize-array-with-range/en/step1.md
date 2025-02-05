# Function to Initialize Array with Range

To initialize an array with a range of numbers, use the following function:

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

This function takes three arguments: `end` (required), `start` (optional, default value is `0`), and `step` (optional, default value is `1`). It returns an array containing the numbers in the specified range, where `start` and `end` are inclusive with their common difference `step`.

To use this function, simply call it with the desired range parameters:

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

This function uses `Array.from()` to create an array of the desired length, and then a map function to fill the array with the desired values in the given range. If you omit the second argument, `start`, it will use a default value of `0`. If you omit the last argument, `step`, it will use a default value of `1`.
