# How to Uppercase Object Keys in JavaScript

To convert all the keys of an object to upper case in JavaScript, follow these steps:

1. Use `Object.keys()` to get an array of the object's keys.
2. Use `Array.prototype.reduce()` to map the array to an object.
3. Use `String.prototype.toUpperCase()` to uppercase the keys.

Here's the code:

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

To test the function, you can call it like this:

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
