# How to Map an Array to an Object in JavaScript

To map an object array to an object in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()` to map the array to an object.
3. Use the `mapKey` parameter to map the keys of the object and the `mapValue` parameter to map the values.

Here's an example code snippet that demonstrates how to use the `objectify` function to map an object array to an object:

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

You can then use the `objectify` function to map an object array to an object in the following ways:

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// Map the object array to an object using the name property as keys
objectify(people, (p) => p.name.toLowerCase());
// Output: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// Map the object array to an object using the name property as keys and the age property as values
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// Output: { john: 42, adam: 39 }
```
