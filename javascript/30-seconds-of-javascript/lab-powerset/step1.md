# How to Generate Powerset in JavaScript

To generate a powerset of a given array of numbers in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.reduce()` method combined with the `Array.prototype.map()` method to iterate over the elements and combine them into an array containing all combinations.
3. Implement the following code:

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. To generate the powerset, call the function `powerset()` and pass in the array as an argument. For example:

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

This will return an array containing all possible subsets of the given array.
