# Group Array Elements

To group elements of arrays based on their position in the original arrays, use the `zip` function provided below.

- Open the Terminal/SSH and type `node` to start practicing coding.
- The `zip` function uses `Math.max()` and `Function.prototype.apply()` to get the longest array in the arguments.
- It creates an array with that length as the return value and uses `Array.from()` with a mapping function to create an array of grouped elements.
- If the lengths of the argument arrays vary, `undefined` is used where no value could be found.

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

Example usage:

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
