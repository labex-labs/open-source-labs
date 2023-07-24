# Creating a Frozen Set Object in JavaScript

To create a frozen `Set` object in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Set` constructor to create a new `Set` object from `iterable`.
3. Set the `add`, `delete`, and `clear` methods of the newly created object to `undefined` to effectively freeze the object.

Here's an example code snippet:

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Output: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

This code creates a frozen `Set` object from an iterable of numbers and returns the object with its `add`, `delete`, and `clear` methods set to `undefined`.
