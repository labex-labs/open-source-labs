# How to Assign Default Values for Object Properties

To assign default values for all properties in an object that are `undefined`, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.assign()` to create a new empty object and copy the original one to maintain key order.
3. Use `Array.prototype.reverse()` and the spread operator (`...`) to combine the default values from left to right.
4. Finally, use `obj` again to overwrite properties that originally had a value.

Here's an example code snippet:

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

This code snippet will return an object that has default values for all properties that were undefined in the original object.
