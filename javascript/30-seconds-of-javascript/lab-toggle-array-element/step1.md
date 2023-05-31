# How to Toggle an Element in an Array

To toggle an element in an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Check if the given element is in the array using `Array.prototype.includes()`.
3. If the element is in the array, use `Array.prototype.filter()` to remove it.
4. If the element is not in the array, use the spread operator (`...`) to push it.
5. Use the `toggleElement` function, which accepts an array and a value, to toggle the element in the array.

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

By following these steps, you can easily toggle an element in an array using JavaScript.
