# Flattening an Object

To flatten an object with paths for keys, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion to flatten the object.
3. Use `Object.keys()` combined with `Array.prototype.reduce()` to convert every leaf node to a flattened path node.
4. If the value of a key is an object, call the function recursively with the appropriate `prefix` to create the path using `Object.assign()`.
5. Otherwise, add the appropriate prefixed key-value pair to the accumulator object.
6. Omit the second argument, `prefix`, unless you want every key to have a prefix.

Here is an example implementation:

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

You can use the `flattenObject` function like this:

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
