# Checking if Array Elements Are Equal with a Given Function

To check if all elements in an array are equal, use the `allEqualBy` function. This function applies a given mapping function `fn` to the first element of the array `arr`. It then checks if `fn` returns the same value for all elements in the array as it did for the first element, using `Array.prototype.every()`. The function uses the strict comparison operator, which does not account for `NaN` self-inequality.

Here's the code for `allEqualBy`:

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

You can use `allEqualBy` like this:

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

To start practicing coding with this function, open the Terminal/SSH and type `node`.
