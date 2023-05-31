# Function to Handle Click Outside of an Element

To execute a callback function whenever a user clicks outside of a specified element, use the `onClickOutside` function. Here are the steps to use it:

1. Open Terminal/SSH and type `node` to start practicing coding.
2. Use `EventTarget.addEventListener()` to listen for `'click'` events.
3. Use `Node.contains()` to check if `Event.target` is a descendant of `element`.
4. If `Event.target` is not a descendant of `element`, execute the `callback` function.

```js
const onClickOutside = (element, callback) => {
  document.addEventListener("click", (e) => {
    if (!element.contains(e.target)) callback();
  });
};
```

To test the `onClickOutside` function, use the following code:

```js
onClickOutside("#my-element", () => console.log("Hello"));
// This will log 'Hello' whenever the user clicks outside of #my-element
```
