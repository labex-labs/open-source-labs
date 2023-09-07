# Object Merge Function

To merge two or more objects, follow the given steps:

1. Open the Terminal/SSH and type `node` to start coding.
2. Use `Array.prototype.reduce()` along with `Object.keys()` to iterate over all objects and keys.
3. Use `Object.prototype.hasOwnProperty()` and `Array.prototype.concat()` to append values for keys existing in multiple objects.
4. Use the given code snippet to create a new object from the combination of two or more objects.

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

For example, consider the following objects:

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

When you merge these two objects using the `merge()` function, you get the following result:

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
