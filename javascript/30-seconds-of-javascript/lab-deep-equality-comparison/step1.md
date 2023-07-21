# How to Check Object Equality in JavaScript

To check if two values are equivalent, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Perform a deep comparison between the two values using the `equals()` function.
3. Check if the two values are identical. If so, return `true`.
4. Check if both values are `Date` objects with the same time, using `Date.prototype.getTime()`. If so, return `true`.
5. Check if both values are non-object values with an equivalent value (strict comparison). If so, return `true`.
6. Check if only one value is `null` or `undefined` or if their prototypes differ. If so, return `false`.
7. If none of the above conditions are met, use `Object.keys()` to check if both values have the same number of keys.
8. Use `Array.prototype.every()` to check if every key in `a` exists in `b` and if they are equivalent by calling `equals()` recursively.

Use the following code to implement the `equals()` function:

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

Use the following code examples to test the `equals()` function:

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
