# Debounce Promise

To create a debounced function that returns a promise, delaying invoking the provided function until at least `ms` milliseconds have elapsed since the last time it was invoked, use the following steps:

1. Every time the debounced function is invoked, clear the current pending timeout with `clearTimeout()`, then use `setTimeout()` to create a new timeout that delays invoking the function until at least `ms` milliseconds has elapsed.
2. Use `Function.prototype.apply()` to apply the `this` context to the function and provide the necessary arguments.
3. Create a new `Promise` and add its `resolve` and `reject` callbacks to the `pending` promises stack.
4. When `setTimeout()` is called, copy the current stack (as it can change between the provided function call and its resolution), clear it and call the provided function.
5. When the provided function resolves/rejects, resolve/reject all promises in the stack (copied when the function was called) with the returned data.
6. Omit the second argument, `ms`, to set the timeout at a default of `0` ms.

Here's the code for the `debouncePromise()` function:

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          },
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

Here's an example of how to use `debouncePromise()`:

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// Will log ['resolved', 'bar'] both times
```
