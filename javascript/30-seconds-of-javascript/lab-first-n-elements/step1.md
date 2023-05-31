# How to Get the First N Elements of an Array in JavaScript

To get the first `n` elements of an array in JavaScript, you can use the `Array.prototype.slice()` method. Here's how:

```js
const firstN = (arr, n) => arr.slice(0, n);
```

In this code snippet, `arr` represents the array you want to extract the elements from, and `n` represents the number of elements you want to extract. The `slice()` method takes two arguments: the start index (which is `0` in this case) and the end index (which is `n`). The method returns a new array containing the extracted elements.

Here's an example of how to use the `firstN()` function:

```js
firstN(["a", "b", "c", "d"], 2); // ['a', 'b']
```

This will return the first two elements of the `['a', 'b', 'c', 'd']` array, which are `['a', 'b']`.
