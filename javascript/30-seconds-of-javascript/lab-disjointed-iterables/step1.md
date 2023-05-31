# Checking for Disjointed Iterables

To check if two iterables have no common values, you can use the `isDisjoint` function.

Here's how to use it:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a new `Set` object from each iterable using the `Set` constructor.
3. Use `Array.prototype.every()` and `Set.prototype.has()` to check that the two iterables have no common values.

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

Here are some examples:

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
