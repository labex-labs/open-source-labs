# Compact Object Algorithm

To deeply remove all falsy values from an object or array, use the following algorithm:

1. Use recursion to call the `compactObject()` function on each nested object or array.
2. Initialize the iterable data using `Array.isArray()`, `Array.prototype.filter()`, and `Boolean()`. This is done to avoid sparse arrays.
3. Use `Object.keys()` and `Array.prototype.reduce()` to iterate over each key with an appropriate initial value.
4. Use `Boolean()` to determine the truthiness of each key's value and add it to the accumulator if it's truthy.
5. Use `typeof` to determine if a given value is an `object` and call the function again to deeply compact it.

Here's the code for the `compactObject()` function:

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {},
  );
};
```

To use this function, pass an object or array as an argument to `compactObject()`. The function will return a new object or array with all falsy values removed.

For example:

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" },
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
