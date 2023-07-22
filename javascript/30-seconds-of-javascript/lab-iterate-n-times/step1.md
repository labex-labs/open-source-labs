# Code Practice: Iterating N Times

To practice coding, open the Terminal/SSH and type `node`. Once you have done that, use the following function to iterate over a callback `n` times:

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

To use this function, call `times()` and pass in the following arguments:

- `n`: the number of times you want to iterate over the callback function
- `fn`: the callback function you want to iterate over
- `context` (optional): the context you want to use for the callback function (if not specified, it will use an `undefined` object or the global object in non-strict mode)

Here's an example of how to use the `times()` function:

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

This will iterate over the callback function `i => (output += i)` 5 times and store the output in the `output` variable. The output will then be logged to the console, which will display `01234`.
