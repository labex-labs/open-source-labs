# How to Rearrange Function Arguments in JavaScript

To rearrange function arguments in JavaScript, you can use the `rearg()` function. First, create a function that invokes the provided function with its arguments arranged according to the specified indexes. You can use `Array.prototype.map()` to reorder arguments based on `indexes`. Then, use the spread operator (`...`) to pass the transformed arguments to `fn`.

Here's an example of how to use the `rearg()` function:

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

In this example, we use `rearg()` to create a new function that rearranges the arguments of another function.

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

In the code above, we create a new function `rearged` that rearranges the arguments of the function `function(a, b, c) { return [a, b, c]; }`. The `indexes` argument specifies the order in which the arguments should be rearranged. In this case, we want the third argument to come first, the first argument to come second, and the second argument to come third. When we call `rearged('b', 'c', 'a')`, it returns `['a', 'b', 'c']`, which is the result of calling the original function with the rearranged arguments.
