# Transform Function Arguments

To transform function arguments, use the `overArgs` function, which creates a new function that invokes the provided function with its arguments transformed.

- To transform the arguments, use `Array.prototype.map()` in combination with the spread operator (`...`) and pass the transformed arguments to `fn`.

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- To test the `overArgs` function, create a sample function and an array of transforms, then call the new function with arguments.

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

To start practicing coding, open the Terminal/SSH and type `node`.
