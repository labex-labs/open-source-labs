# Function to Check if Value Is of Type

To check if a provided value is of a specified type, follow these steps:

- Ensure that the value is not `undefined` or `null` by using `Array.prototype.includes()`.
- Use `Object.prototype.constructor` to compare the constructor property on the value with the specified `type`.
- The function `is()` below performs these checks and returns `true` if the value is of the specified type, and `false` otherwise.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

You can use `is()` to check if a value is of various types, such as `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number`, and `Boolean`. For example:

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
