# How to Use Array.prototype.filter() to Create a Compact Array

To create a compact array in JavaScript, you can use the `Array.prototype.filter()` method to remove any falsy values from the array. Falsy values include `false`, `null`, `0`, `""`, `undefined`, and `NaN`.

Here's an example code snippet that demonstrates how to create a compact array using `Array.prototype.filter()`:

```js
const compact = (arr) => arr.filter(Boolean);
```

You can then use the `compact` function to create a compact array by passing in an array as an argument. For example:

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// Output: [ 1, 2, 3, 'a', 's', 34 ]
```

By using `Array.prototype.filter()` in this way, you can easily create a compact array that only contains truthy values.
