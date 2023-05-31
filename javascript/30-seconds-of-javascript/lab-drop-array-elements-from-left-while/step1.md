# Array Elements Removal Based on Function

To remove specific elements from an array, use the `dropWhile` function, which removes elements until the passed function returns `true`. The function then returns the remaining elements in the array.

Here's how it works:

- Loop through the array using `Array.prototype.slice()` to drop the first element of the array until the value returned from `func` is `true`.
- Return the remaining elements.

Example usage:

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

To start practicing coding, open the Terminal/SSH and type `node`.
