# Function to Bind Object Method

To create a function that binds an object method to its context and optionally prepends additional parameters, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Define a function that takes three parameters: the object context, the method key, and any additional arguments to be prepended.
3. The function should return a new function that uses `Function.prototype.apply()` to bind the method to the object context.
4. Use the spread operator (`...`) to prepend any additional supplied parameters to the arguments.
5. Here's an example implementation:

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. To test the function, create an object with a method and bind it using `bindKey()`. Then, call the bound method with some arguments.

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  },
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
