# Instructions to Pluck Values From an Array of Objects

To pluck values from an array of objects, you can follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` to map the array of objects to the value of a specified `key` for each object.
3. Implement the following function:

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. Test the function with an example array of objects:

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

This will return an array of values corresponding to the specified `key` from the array of objects.
