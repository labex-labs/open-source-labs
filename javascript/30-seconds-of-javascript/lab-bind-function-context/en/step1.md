# Creating a Function with a Given Context

To create a function with a given context, use the `bind` function. First, open the Terminal/SSH and type `node`.

The `bind` function creates a new function that invokes the original function with a given context. It can also optionally prepend any additional supplied parameters to the arguments.

To use `bind`, pass in the original function (`fn`) and the desired context (`context`). You can also pass in any additional parameters that should be bound to the function (`...boundArgs`).

The `bind` function returns a new function that uses `Function.prototype.apply()` to apply the given `context` to `fn`. It also uses the spread operator (`...`) to prepend any additional supplied parameters to the arguments.

Here is an example usage of `bind`:

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

In this example, we define a `greet` function that takes two parameters (`greeting` and `punctuation`) and returns a string that concatenates the `greeting`, the `user` property of the current context (`this`), and the `punctuation`.

We then create a new object (`freddy`) that has a `user` property set to `'fred'`.

Finally, we create a new function (`freddyBound`) using `bind`, passing in the `greet` function and the `freddy` object as the desired context. We can then call `freddyBound` with two additional parameters (`'hi'` and `'!'`), which get passed through to the original `greet` function along with the bound `freddy` context. The resulting output is `'hi fred!'`.
