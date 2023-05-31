# How to Call Functions with Context in JavaScript

To execute code in Node.js, open the Terminal/SSH and type `node`. If you want to call a function with a specific context and a set of arguments in JavaScript, you can use a closure. Here's how you can do it:

1. Define a function called `call` that takes a `key` and a set of `args` as parameters and returns a new function that takes a `context` parameter.

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. Use the `call` function to call the `map` function on an array of numbers. In this example, the `map` function doubles each number in the array.

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. You can also bind the `call` function to a specific key, such as `map`, and use it to call the `map` function on an array of numbers.

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

By using the `call` function, you can easily call any function with a specific context and set of arguments.
