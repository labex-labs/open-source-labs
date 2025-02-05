# Check if a Value is a Plain Object

To check if a value is a plain object, follow these steps:

- Check if the value is truthy.
- Use `typeof` to check if it is an object.
- Use `Object.prototype.constructor` to make sure the constructor is equal to `Object`.

Use the following code to implement this check:

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

You can test this function with the following examples:

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

To start practicing coding, open the Terminal/SSH and type `node`.
