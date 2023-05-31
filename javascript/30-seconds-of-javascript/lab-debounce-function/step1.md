# Debounce Function

To create a debounced function that delays invoking the provided function until at least `ms` milliseconds have elapsed since its last invocation, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Each time the debounced function is invoked, clear the current pending timeout with `clearTimeout()`. Use `setTimeout()` to create a new timeout that delays invoking the function until at least `ms` milliseconds have elapsed.
3. Use `Function.prototype.apply()` to apply the `this` context to the function and provide the necessary arguments.
4. Omit the second argument, `ms`, to set the timeout at a default of `0` ms.

Here's an example of how to use the `debounce` function:

```js
const debounce = (fn, ms = 0) => {
  let timeoutId;
  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn.apply(this, args), ms);
  };
};

window.addEventListener(
  "resize",
  debounce(() => {
    console.log(window.innerWidth);
    console.log(window.innerHeight);
  }, 250)
); // Will log the window dimensions at most every 250ms
```
