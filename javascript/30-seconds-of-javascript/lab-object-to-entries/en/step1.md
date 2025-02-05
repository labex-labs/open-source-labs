# Converting an Object to an Array of Key-Value Pairs

To convert an object into an array of key-value pairs, use the `Object.keys()` method and the `Array.prototype.map()` method. This will iterate over the object's keys and produce an array with key-value pairs. Alternatively, you can use the `Object.entries()` method, which provides similar functionality.

Here's an example code snippet that shows how to convert an object to an array of key-value pairs:

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

You can use the `objectToEntries()` function to convert an object to an array of key-value pairs like this:

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
