# How to Observe Element Mutations

To observe mutations on an element, you can use a `MutationObserver` and the `observeMutations` function provided below.

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `MutationObserver` to observe mutations on the given element.
3. Use `Array.prototype.forEach()` to run the callback for each mutation that is observed.
4. Omit the third argument, `options`, to use the default options (all `true`).
5. Copy the `observeMutations` function below and paste it into your code.
6. Call the `observeMutations` function with the desired element and callback function as arguments.
7. The `observeMutations` function will return an observer object.
8. Call the `disconnect()` method on the observer object to stop logging mutations on the page.

```js
const observeMutations = (element, callback, options) => {
  const observer = new MutationObserver((mutations) =>
    mutations.forEach((m) => callback(m))
  );
  observer.observe(
    element,
    Object.assign(
      {
        childList: true,
        attributes: true,
        attributeOldValue: true,
        characterData: true,
        characterDataOldValue: true,
        subtree: true,
      },
      options
    )
  );
  return observer;
};
```

Example usage:

```js
const obs = observeMutations(document, console.log);
// Logs all mutations that happen on the page
obs.disconnect();
// Disconnects the observer and stops logging mutations on the page
```
