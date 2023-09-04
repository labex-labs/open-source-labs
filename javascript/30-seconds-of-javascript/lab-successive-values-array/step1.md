# Array of Successive Values

To create an array of successive values in JavaScript, you can use the `Array.prototype.reduce()` method. This method applies a function to an accumulator and each element in the array, from left to right, and returns an array of the successively reduced values.

Here's how to use `reduceSuccessive` function to apply the given function to the given array, storing each new result:

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc],
  );
```

You can then call the `reduceSuccessive` function with an array, a function, and an initial value for the accumulator:

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

To start practicing coding with this function, open the Terminal/SSH and type `node`.
