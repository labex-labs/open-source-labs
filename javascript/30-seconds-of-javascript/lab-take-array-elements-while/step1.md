# Removing Array Elements Based on a Condition

To remove elements in an array based on a condition, open the Terminal/SSH and type `node`.

The `takeWhile` function removes elements in an array until the passed function returns `false`, and then returns the removed elements.

Here are the steps to use the `takeWhile` function:

- Loop through the array using a `for...of` loop over `Array.prototype.entries()`.
- Loop until the returned value from the function is falsy.
- Return the removed elements using `Array.prototype.slice()`.
- The `fn` callback function accepts a single argument which is the value of the element.

Use the following code to implement the `takeWhile` function:

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

Here is an example of using the `takeWhile` function to remove elements from an array based on a condition:

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
