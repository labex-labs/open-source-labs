# Instructions for Converting Map to Object in JavaScript

To convert a JavaScript `Map` to an object, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Map.prototype.entries()` method to convert the `Map` to an array of key-value pairs.
3. Use the `Object.fromEntries()` method to convert the array to an object.

Here is an example code snippet for converting a `Map` to an object:

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

To test the function, you can run:

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2],
  ])
); // {a: 1, b: 2}
```
