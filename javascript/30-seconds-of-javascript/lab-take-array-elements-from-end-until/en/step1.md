# Removing Array Elements From the End Until a Condition is Met

To start practicing coding, open the Terminal/SSH and type `node`.

This function removes elements from the end of an array until the passed function returns `true` and then it returns the removed elements.

Here's how it works:

- First, create a reversed copy of the array using the spread operator (`...`) and `Array.prototype.reverse()`.
- Next, loop through the reversed copy using a `for...of` loop over `Array.prototype.entries()` until the returned value from the function is truthy.
- After that, return the removed elements using `Array.prototype.slice()`.
- The callback function, `fn`, accepts a single argument which is the value of the element.

Here's the code:

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Here's an example of how to use this function:

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
