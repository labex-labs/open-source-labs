# Checking for Equality of Array Elements

To check if all the elements in an array are the same, you can use the `Array.prototype.every()` method, which compares all elements with the first one.

Here's how you can implement it:

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

Note that the `strict comparison` operator is used to compare the elements. This operator doesn't account for `NaN` self-inequality.

Example usage:

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
