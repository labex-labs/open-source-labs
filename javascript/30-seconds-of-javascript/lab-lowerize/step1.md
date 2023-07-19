# Converting Object Keys to Lowercase

To convert all keys of an object to lowercase, follow these steps:

1. Open the Terminal/SSH to start practicing coding and type `node`.
2. Use `Object.keys()` to obtain an array of the object's keys.
3. Use `Array.prototype.reduce()` to map the array to an object.
4. Use `String.prototype.toLowerCase()` to lowercase the keys.

Here is an example code that implements these steps:

```js
const lowerize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toLowerCase()] = obj[k];
    return acc;
  }, {});
```

You can then call the `lowerize()` function with an object as an argument to get a new object with all keys in lowercase. For example:

```js
lowerize({ Name: "John", Age: 22 }); // { name: 'John', age: 22 }
```
