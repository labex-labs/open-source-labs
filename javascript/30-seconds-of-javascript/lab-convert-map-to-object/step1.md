# Convert Map to Object

> To start practicing coding, open the Terminal/SSH and type `node`.

Converts a `Map` to an object.

- Use `Map.prototype.entries()` to convert the `Map` to an array of key-value pairs.
- Use `Object.fromEntries()` to convert the array to an object.

```js
const mapToObject = map => Object.fromEntries(map.entries());
```

```js
mapToObject(new Map([['a', 1], ['b', 2]])); // {a: 1, b: 2}
```
