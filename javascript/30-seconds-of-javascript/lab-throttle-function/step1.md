# Throttle Function

To use the throttle function, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. The throttle function creates a throttled function that only invokes the provided function at most once per every `wait` milliseconds.
4. To create the throttled function, use `setTimeout()` and `clearTimeout()` to throttle the given method, `fn`.
5. Use `Function.prototype.apply()` to apply the `this` context to the function and provide the necessary `arguments`.
6. Use `Date.now()` to keep track of the last time the throttled function was invoked.
7. Use a variable, `inThrottle`, to prevent a race condition between the first execution of `fn` and the next loop.
8. Omit the second argument, `wait`, to set the timeout at a default of `0` ms.

Here is an example of using the throttle function:

```js
window.addEventListener(
  "resize",
  throttle(function (evt) {
    console.log(window.innerWidth);
    console.log(window.innerHeight);
  }, 250)
); // Will log the window dimensions at most every 250ms
```
