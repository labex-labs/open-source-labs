# Here's how to iterate over an object's own properties in reverse

To iterate over an object's own properties in reverse order and run a callback for each one, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` to get all the properties of the object.
3. Use `Array.prototype.reverse()` to reverse the order of the properties.
4. Use `Array.prototype.forEach()` to run the provided function for each key-value pair.
5. The callback function should have three arguments: the value, the key, and the object.

Here's the code:

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

You can use this function with any object and callback function. For example, to log the values of `{ foo: 'bar', a: 1 }` in reverse order, you can use the following code:

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
