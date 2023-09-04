# How to Partition an Array into Two Based on a Function

To partition an array into two based on a provided function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()` to create an array of two arrays.
3. Use `Array.prototype.push()` to add elements for which `fn` returns `true` to the first array and elements for which `fn` returns `false` to the second one.

Here's the code you can use:

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []],
  );
```

To test this code, you can use the following example:

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true },
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

This will return an array of two arrays, where the first array contains all the elements for which the provided function returns `true`, and the second array contains all the elements for which the provided function returns `false`.
