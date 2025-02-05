# Function to Check if One Set is a Superset of Another Set

To check if one set is a superset of another set, use the `superSet()` function. First, open the Terminal/SSH and type `node` to start practicing coding. Then, use the following steps:

- Create a new `Set` object from each iterable using the `Set` constructor.
- Use `Array.prototype.every()` and `Set.prototype.has()` to check that each value in the second iterable is contained in the first one.
- The function returns `true` if the first iterable is a superset of the second one, excluding duplicate values. Otherwise, it returns `false`.

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

Use `superSet()` with two sets as arguments to check if one set is a superset of another set.

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
