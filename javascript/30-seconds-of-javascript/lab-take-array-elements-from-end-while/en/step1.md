# Removing Array Elements From the End Until a Condition Is Met

To start practicing coding, open the Terminal/SSH and type `node`.

Here's a function that removes elements from the end of an array until the passed function returns `false`. It then returns the removed elements.

To use it, create a reversed copy of the array using the spread operator (`...`) and `Array.prototype.reverse()`. Then, loop through the reversed copy using a `for...of` loop over `Array.prototype.entries()` until the returned value from the function is falsy.

The callback function, `fn`, accepts a single argument which is the value of the element. Finally, return the removed elements using `Array.prototype.slice()`.

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Here's an example of how to use the function:

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
