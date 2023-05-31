# Function to Initialize an Array with Specified Values

To start practicing coding, open the Terminal/SSH and type `node`.

This function initializes an array with the specified values:

- Use the `Array()` constructor to create an array of the desired length.
- Use `Array.prototype.fill()` to fill it with the desired values.
- If no value is specified, it defaults to `0`.

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

Example usage:

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
