# How to Iterate Over an Object's Own Properties in JavaScript

To iterate over an object's own properties and practice coding, follow these steps:

1. Open the Terminal or SSH.
2. Type `node` to start a new Node.js session.
3. Use the `Object.keys()` method to retrieve an array of the object's own properties.
4. Use the `Array.prototype.forEach()` method to loop over each property and execute a provided function.
5. The provided function should accept three arguments: the property value, the property key, and the object itself.
6. Use the `forOwn()` function with the object and the provided function to iterate over the object's properties.

Here is an example code snippet:

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

This code will log the values of the `foo` and `a` properties to the console.
