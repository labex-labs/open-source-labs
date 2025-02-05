# Creating a Promise with a Delay

To create a new promise that resolves after a specific amount of time, follow these steps:

1. Use the `Promise` constructor to create a new promise.
2. Inside the promise's executor function, use `setTimeout()` to call the promise's `resolve` function with the provided `value` after the specified `delay`.

Here's an example implementation of `resolveAfter()`:

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

Now you can call `resolveAfter()` to get a promise that resolves to the provided value after the specified delay:

```js
resolveAfter("Hello", 1000);
// Returns a promise that resolves to 'Hello' after 1s
```

To start practicing coding, open the Terminal or SSH and type `node`.
