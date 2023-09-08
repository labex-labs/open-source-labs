# Instructions to Deep Clone an Object

To deep clone an object, follow these steps:

1. Create a new terminal/SSH instance and type `node` to start practicing coding.
2. Use recursion to clone primitives, arrays, and objects, excluding class instances.
3. Check if the passed object is `null` and, if so, return `null`.
4. Use `Object.assign()` and an empty object (`{}`) to create a shallow clone of the original.
5. Use `Object.keys()` and `Array.prototype.forEach()` to determine which key-value pairs need to be deep cloned.
6. If the object is an `Array`, set the `clone`'s `length` to that of the original and use `Array.from()` to create a clone.
7. Use the following code to implement deep cloning:

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

Use the following code to test your deep cloning function:

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a !== b, a.obj !== b.obj
```
