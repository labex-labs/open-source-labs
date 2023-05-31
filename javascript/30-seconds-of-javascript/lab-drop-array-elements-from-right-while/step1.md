# Dropping Array Elements from Right Based on Function

To drop elements from the end of an array until a certain condition is met, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Loop through the array using `Array.prototype.slice()` to drop the last element of the array until the passed `func` returns `true`.
3. Return the remaining elements in the array.

Here's an example implementation:

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

You can use this function like this:

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
