# Linear Search Algorithm

To practice coding, open the Terminal or SSH and type `node`. The linear search algorithm finds the first index of a given element in an array.

Here's how it works:

- Use a `for...in` loop to iterate over the indexes of the given array.
- Check if the element in the corresponding index is equal to `item`.
- If the element is found, return the index. Use the unary `+` operator to convert it from a string to a number.
- If the element is not found after iterating over the whole array, return `-1`.

Here's the code:

```js
const linearSearch = (arr, item) => {
  for (const i in arr) {
    if (arr[i] === item) return +i;
  }
  return -1;
};
```

To test the function, call it with an array and a value to search for:

```js
linearSearch([2, 9, 9], 9); // 1
linearSearch([2, 9, 9], 7); // -1
```
