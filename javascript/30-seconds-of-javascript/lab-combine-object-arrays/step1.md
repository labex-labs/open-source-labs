# Function to Combine Object Arrays Based on a Specified Key

To combine two arrays of objects based on a specific key, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()` with an object accumulator to combine all objects in both arrays based on the given `prop`.
3. Use `Object.values()` to convert the resulting object to an array and return it.

Here's the function that you can use:

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {}),
  );
```

Here's an example of how to use this function:

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" },
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
