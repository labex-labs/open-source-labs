# How to Rename Object Keys in JavaScript

To rename multiple object keys with the values provided, you can use the `renameKeys` function. Here are the steps you need to follow:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` in combination with `Array.prototype.reduce()` and the spread operator (`...`) to get the object's keys and rename them according to `keysMap`.
3. Pass the `keysMap` and object (`obj`) as arguments to the `renameKeys` function.
4. The `renameKeys` function returns a new object with the renamed keys.

Here's an example of how to use the `renameKeys` function:

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
