# How to Count Occurrences in JavaScript

To count the number of times a specific value occurs in a JavaScript array, you can use the `Array.prototype.reduce()` method.

Here is how you can do it:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Copy and paste the following code:

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. In the code above, the `countOccurrences` function takes two arguments: the array to search and the value to count.
4. The `reduce()` method is used to loop through each element in the array and increment a counter each time the specific value is encountered.
5. To test the function, call it with an array and a value, like this:

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

This will return the number of times `1` occurs in the array `[1, 1, 2, 1, 2, 3]`, which is `3`.
