# Checking If All Elements in an Array Are Unique with a Function

To check if all elements in an array are unique based on a provided mapping function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.map()` method to apply the provided function `fn` to all elements in the `arr` array.
3. Create a new `Set` from the mapped values to keep only unique occurrences.
4. Compare the length of the unique mapped values to the original array length using the `Array.prototype.length` and `Set.prototype.size` methods.

Here is the code:

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

You can use the `allUniqueBy()` function to check if all elements in an array are unique. For example:

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
