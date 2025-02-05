# Converting Values to Arrays in JavaScript

To convert a value into an array, use the `castArray` function provided below.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

To use this function, pass the value you want to convert as the argument. The function will check if the value is already an array using `Array.isArray()`. If it is an array, the function will return it as-is. If it is not an array, the function will return the value encapsulated in an array.

Here's an example of how to use `castArray`:

```js
castArray("foo"); // returns: ['foo']
castArray([1]); // returns: [1]
```

To start practicing coding in JavaScript, open the Terminal or SSH and type `node`.
