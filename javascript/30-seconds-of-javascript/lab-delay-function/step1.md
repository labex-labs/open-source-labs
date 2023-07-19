# How to Delay Function Execution in JavaScript

To delay the execution of a function in JavaScript, you can use the `setTimeout()` method. Here's how to do it:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the following syntax to delay the execution of a function `fn` by `ms` milliseconds:

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. To pass arguments to the function, use the spread (`...`) operator like this:

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "later"
); // Logs 'later' after one second.
```

With this code, the provided function `fn` will be invoked after the specified number of milliseconds (`ms`). The `...args` parameter allows you to pass an arbitrary number of arguments to the function.
