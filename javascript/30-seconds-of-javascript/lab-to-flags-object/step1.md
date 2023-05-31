# Converting Array to Flags Object

If you want to start practicing coding, open the Terminal/SSH and type `node`.

The following function converts an array of strings into an object that maps to true.

To do this, we use `Array.prototype.reduce()`. This method converts the array into an object, where each array value serves as a key whose value is set to `true`.

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

Here's an example:

```js
flags(["red", "green"]); // { red: true, green: true }
```
