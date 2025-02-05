# How to Check if All Array Elements Are Unique

To check if all elements in an array are unique, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a new `Set` from the mapped values to keep only unique occurrences.
3. Use `Array.prototype.length` and `Set.prototype.size` to compare the length of the unique values to the original array.

Here's an example function that implements these steps:

```js
const allUnique = (arr) => arr.length === new Set(arr).size;
```

You can use this function to check if an array has all unique elements like this:

```js
allUnique([1, 2, 3, 4]); // true
allUnique([1, 1, 2, 3]); // false
```
