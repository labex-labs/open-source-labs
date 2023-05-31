# Resolve Promise After Given Amount of Time

> To start practicing coding, open the Terminal/SSH and type `node`.

Creates a promise that resolves after a given amount of time to the provided value.

- Use the `Promise` constructor to create a new promise.
- Use `setTimeout()` to call the promise's `resolve` function with the passed `value` after the specified `delay`.

```js
const resolveAfter = (value, delay) =>
  new Promise(resolve => {
    setTimeout(() => resolve(value, delay));
  });
```

```js
resolveAfter('Hello', 1000);
// Returns a promise that resolves to 'Hello' after 1s
```
