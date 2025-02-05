# Instructions for Picking Object Keys

To pick specific key-value pairs from an object, use the function `pick(obj, arr)`.

- Pass in the object as the first argument and an array of keys to pick as the second argument.
- The function returns a new object with only the key-value pairs that correspond to the given keys.

Here's an example of how to use `pick()`:

```js
const pick = (obj, arr) =>
  arr.reduce((acc, curr) => (curr in obj && (acc[curr] = obj[curr]), acc), {});

pick({ a: 1, b: "2", c: 3 }, ["a", "c"]); // { 'a': 1, 'c': 3 }
```

To get started with coding practice, open the Terminal/SSH and type `node`.
