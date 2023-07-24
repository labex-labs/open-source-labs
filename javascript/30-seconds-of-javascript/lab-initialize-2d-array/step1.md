# Initializing a 2D Array in JavaScript

To initialize a 2D array in JavaScript, you can use the following code:

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

This code uses `Array.from()` and `Array.prototype.map()` to create an array of `height` rows, where each row is a new array of `width` length. It also uses `Array.prototype.fill()` to set all items in the array to the `value` parameter. If no `value` is provided, it defaults to `null`.

You can call the function like this:

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

This will create a 2D array with width of 2, height of 2, and all values set to 0.
