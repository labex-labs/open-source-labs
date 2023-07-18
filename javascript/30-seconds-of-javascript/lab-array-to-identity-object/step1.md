# Here's how to convert an array to an identity object

If you want to practice coding, open the Terminal/SSH and type `node`. To convert an array of values into an object with the same values as keys and values, follow these steps:

1. Use `Array.prototype.map()` to map each value to an array of key-value pairs.
2. Use `Object.fromEntries()` to convert the array of key-value pairs into an object.

Here's the code:

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

And here's an example:

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
