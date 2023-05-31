# How to Group an Array into an Object

To group an array into an object, follow these steps:

1. Open the Terminal or SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.reduce()` method to build an object from the two arrays.
3. Provide an array of valid property identifiers and an array of values.
4. If the length of the property array is longer than the value array, the remaining keys will be set to `undefined`.
5. If the length of the value array is longer than the property array, the remaining values will be ignored.

Here is an example code snippet that demonstrates how to group an array into an object:

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
