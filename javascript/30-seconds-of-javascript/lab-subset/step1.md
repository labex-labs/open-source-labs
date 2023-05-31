# Checking if a Subset of an Iterable is Contained in Another Iterable

To practice coding, open the Terminal/SSH and type `node`. This function checks whether the first iterable is a subset of the second iterable, excluding duplicate values.

To achieve this, you can do the following:

- Create a new `Set` object from each iterable using the `Set` constructor.
- Use `Array.prototype.every()` and `Set.prototype.has()` to check if every value in the first iterable is contained in the second iterable.

Here's an example implementation:

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

You can use the `subSet` function by passing in two sets to compare. For example:

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
