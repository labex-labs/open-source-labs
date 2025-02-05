# Function to Invert an Object

To invert the key-value pairs of an object without altering the original object, use the `invertKeyValues` function.

- Call the function by typing `invertKeyValues(obj, fn)` in the Terminal/SSH, where `obj` is the object to be inverted and `fn` is an optional function to be applied to the inverted key.

- The `Object.keys()` and `Array.prototype.reduce()` methods are used to create a new object with inverted key-value pairs, and if a function is provided, it is applied to each inverted key.

- If `fn` is omitted, the function returns only the inverted keys without any function applied to them.

- The function returns an object with each inverted value being an array of keys responsible for generating the inverted value.

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

Example usage:

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
