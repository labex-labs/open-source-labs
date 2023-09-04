# Promisify Function

To convert an asynchronous function to return a promise, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use currying to return a function that returns a `Promise` which calls the original function.
3. Use the rest operator (`...`) to pass in all the parameters.
4. If you are using Node 8+, you can use [`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original).
5. Here's an example code snippet:

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result))),
    );
```

6. To use this function, define the asynchronous function and pass it as a parameter to the `promisify` function. The returned function will now return a promise.

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // Promise resolves after 2s
```

The `delay` function is an example of an asynchronous function that now returns a promise using the `promisify` function.
