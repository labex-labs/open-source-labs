# Handling Scroll Stop

To start coding, open the Terminal/SSH and type `node`.

This script runs a callback function when the user stops scrolling:

- Use `EventTarget.addEventListener()` to listen for the `'scroll'` event.
- Use `setTimeout()` to wait `150` ms before calling the given `callback`.
- Use `clearTimeout()` to clear the timeout if a new `'scroll'` event is fired in under `150` ms.

```js
const handleScrollStop = (callback) => {
  let scrollTimeout;
  window.addEventListener(
    "scroll",
    (e) => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        callback();
      }, 150);
    },
    false
  );
};
```

```js
handleScrollStop(() => {
  console.log("The user has stopped scrolling.");
});
```
