# How to Pull Values from an Array based on a Given Function

To start practicing coding, open the Terminal/SSH and type `node`.

The function `pullBy` mutates the original array by filtering out the specified values based on a given iterator function. Here's how it works:

1. Check if the last argument provided is a function.
2. Use `Array.prototype.map()` to apply the iterator function `fn` to all array elements.
3. Use `Array.prototype.filter()` and `Array.prototype.includes()` to pull out the values that are not needed.
4. Set `Array.prototype.length` to reset the passed-in array's length to `0`.
5. Use `Array.prototype.push()` to re-populate it with only the pulled values.

Here's the code:

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val),
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

And here's an example of how to use it:

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

Note that in this example, we're pulling out all elements with an `x` property of `1` or `3`. The resulting `myArray` will only contain the element with an `x` property of `2`.
