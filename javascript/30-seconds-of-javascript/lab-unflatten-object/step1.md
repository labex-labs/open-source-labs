# How to Unflatten an Object in JavaScript

To unflatten an object with paths for keys in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use nested `Array.prototype.reduce()` to convert the flat path to a leaf node.

3. Use `String.prototype.split()` to split each key with a dot delimiter and `Array.prototype.reduce()` to add objects against the keys.

4. If the current accumulator already contains a value against a particular key, return its value as the next accumulator.

5. Otherwise, add the appropriate key-value pair to the accumulator object and return the value as the accumulator.

Here's the code for the `unflattenObject` function:

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res,
    );
    return res;
  }, {});
```

You can use the `unflattenObject` function to unflatten an object in JavaScript:

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
