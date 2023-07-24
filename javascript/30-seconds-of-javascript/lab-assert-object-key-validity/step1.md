# Validate Object Keys

To ensure that all keys in an object match the specified `keys`, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `Object.keys()` to retrieve the keys of the object, `obj`.
- Use `Array.prototype.every()` and `Array.prototype.includes()` to validate that each key in the object is included in the `keys` array.

Here's an example implementation:

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

You can use the function like this:

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
