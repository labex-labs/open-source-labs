# Here's how to Convert Object to Map

To convert an object to a `Map`, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.entries()` to convert the object to an array of key-value pairs.
3. Use the `Map` constructor to convert the array to a `Map`.

Here's an example code snippet:

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

You can use the `objectToMap()` function to convert an object to a `Map`. For example:

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
