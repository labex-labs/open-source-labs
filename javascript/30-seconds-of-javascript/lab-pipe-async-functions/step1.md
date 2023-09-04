# How to Pipe Async Functions in JavaScript

To start practicing coding with JavaScript, open the Terminal/SSH and type `node`. Once you're familiar with the basics, you can start working with asynchronous functions.

The `pipeAsyncFunctions` function allows you to perform left-to-right function composition with asynchronous functions. Here's how it works:

- The function takes in any number of asynchronous functions as arguments.
- The spread operator (`...`) is used to pass these functions as separate arguments to the `pipeAsyncFunctions` function.
- The resulting function can accept any number of arguments, but each of the functions being composed must accept a single argument.
- The functions can return a combination of normal values, Promises, or be `async` and return through `await`.
- The `reduce()` method is used along with `Promise.prototype.then()` to perform function composition.
- The `reduce()` method iterates over the functions, executing each one in sequence and passing the result of one function to the next.
- The resulting Promise is returned.

Here's an example of how to use `pipeAsyncFunctions` to sum a number:

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4,
);
(async () => {
  console.log(await sum(5)); // 15 (after one second)
})();
```

In this example, `sum` is composed of four functions that add different values to the input number. The final value of `sum` is the result of executing each function in sequence, with a delay of one second for the second function. The `async` keyword is used with the last function to allow for the use of `await`.

By using `pipeAsyncFunctions`, you can easily compose any number of asynchronous functions together to create more complex functionality.
