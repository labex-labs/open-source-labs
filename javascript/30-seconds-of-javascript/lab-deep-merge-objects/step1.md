# Revised: How to Deep Merge Objects in JavaScript

To deeply merge two objects in JavaScript, you can use the `deepMerge` function. This function takes two objects and a function as arguments. The function is used to handle keys present in both objects.

Here's how the `deepMerge` function works:

1. Use `Object.keys()` to get the keys of both objects, create a `Set` from them and use the spread operator (`...`) to create an array of all the unique keys.
2. Use `Array.prototype.reduce()` to add each unique key to the object, using `fn` to combine the values of the two given objects.

Here's the code for the `deepMerge` function:

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

To use the `deepMerge` function, call it with two objects and a function. Here's an example:

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

In this example, the `deepMerge` function is used to merge two objects. The resulting object has the values of both objects merged together.
