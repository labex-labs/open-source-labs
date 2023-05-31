# Removing Matching Elements from an Array

To remove specific elements from an array based on a given condition, you can use the `remove` function. This function mutates the original array by removing elements for which the given function returns `false`.

Here are the steps to use the `remove` function:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` to find array elements that return truthy values.
3. Use `Array.prototype.reduce()` to remove elements using `Array.prototype.splice()`.
4. The callback function is invoked with three arguments (value, index, array).

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

Here's an example of using the `remove` function:

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

This will return a new array with the removed elements.
