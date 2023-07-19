# Object Transformation

To start practicing coding, open the Terminal/SSH and type `node`.

The `transform` function applies a specified function against an accumulator and each key in the object, from left to right. Here's how to use it:

- Use `Object.keys()` to iterate over each key in the object.
- Use `Array.prototype.reduce()` to apply the specified function against the given accumulator.

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

Here's an example:

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
