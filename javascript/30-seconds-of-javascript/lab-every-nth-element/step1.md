# Function to Return Every NTH Element of an Array

To return every `nth` element in an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.filter()` method to create a new array that contains every `nth` element of a given array.
3. Use the following function to implement the above step:

```js
const everyNth = (arr, nth) => arr.filter((e, i) => i % nth === nth - 1);
```

4. To test the function, use the following code:

```js
everyNth([1, 2, 3, 4, 5, 6], 2); // [ 2, 4, 6 ]
```

This will return a new array with every second element of the input array.
