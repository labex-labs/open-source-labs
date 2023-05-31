# Convert Array to Identity Object

> To start practicing coding, open the Terminal/SSH and type `node`.

Converts an array of values into an object with the same values as keys and values.

- Use `Array.prototype.map()` to map each value to an array of key-value pairs.
- Use `Object.fromEntries()` to convert the array of key-value pairs into an object.

```js
const toIdentityObject = arr => Object.fromEntries(arr.map(v => [v, v]));
```

```js
toIdentityObject(['a', 'b']); // { a: 'a', b: 'b' }
```
