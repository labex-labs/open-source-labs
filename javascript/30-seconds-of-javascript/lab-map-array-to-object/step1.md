# Mapping Array to Object

To map the values of an array to an object using a function, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding practice.
2. Use `Array.prototype.reduce()` to apply `fn` to each element in `arr` and combine the results into an object.
3. Use `el` as the key for each property and the result of `fn` as the value.

Here is an example code snippet:

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

You can use the `mapObject` function as shown in this example:

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
