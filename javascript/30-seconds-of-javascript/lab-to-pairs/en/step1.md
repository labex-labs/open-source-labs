# Converting an Object to Pairs

To convert an object to an array of key-value pairs, use the `toPairs` function. To get started with coding, open the Terminal/SSH and type `node`.

The `toPairs` function works in the following way:

- First, it checks if `Symbol.iterator` is defined for the given iterable object.
- If `Symbol.iterator` is defined, it uses `Array.prototype.entries()` to get an iterator for the object and then converts the result to an array of key-value pair arrays using `Array.from()`.
- If `Symbol.iterator` is not defined for the object, it uses `Object.entries()` instead.

Here's the code for the `toPairs` function:

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

You can use the `toPairs` function with various types of objects, such as:

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0', 's'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
