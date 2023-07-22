# Converting an Object into an Array of Key-Value Pairs

To convert an object into an array of key-value pairs, you can follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Object.entries()` method to obtain an array of key-value pair arrays from the object.
3. Create a function called `objectToPairs` that accepts an object as an argument and returns the array of key-value pairs.
4. Call the `objectToPairs` function with an example object to test the output.

Here's an example implementation:

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

By following these steps, you can easily convert an object into an array of key-value pairs using JavaScript.
