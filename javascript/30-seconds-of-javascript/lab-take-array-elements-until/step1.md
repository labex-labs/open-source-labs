# Removing Array Elements Until a Condition is Met

To remove elements in an array until a condition is met and get the removed elements, follow the steps below:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Loop through the array using a `for...of` loop over `Array.prototype.entries()` until the function passed as an argument returns a truthy value.
- Use `Array.prototype.slice()` to return the removed elements.
- The callback function, `fn`, accepts a single argument which is the value of the element.

Here's an example code snippet:

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

In the above example, the `takeUntil()` function is used to remove elements in the `[1, 2, 3, 4]` array until the value is greater than or equal to 3. The output is `[1, 2]`.
