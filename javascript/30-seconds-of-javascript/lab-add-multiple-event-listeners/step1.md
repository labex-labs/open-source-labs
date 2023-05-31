# How to Add Multiple Event Listeners to an Element

To add multiple event listeners to an element with the same handler in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Define a function called `addMultipleListeners` that takes in parameters for the element, an array of event types, a listener callback function, and optional arguments for the `addEventListener()` method.
3. Inside the `addMultipleListeners` function, use `Array.prototype.forEach()` to iterate over the array of event types and call `addEventListener()` for each event type with the listener and optional arguments.
4. Call the `addMultipleListeners` function with the element you want to add the event listeners to, an array of event types, and the listener callback function.

Here's an example implementation of the `addMultipleListeners` function:

```js
const addMultipleListeners = (el, types, listener, options, useCapture) => {
  types.forEach((type) =>
    el.addEventListener(type, listener, options, useCapture)
  );
};
```

And here's an example usage of the `addMultipleListeners` function:

```js
addMultipleListeners(
  document.querySelector(".my-element"),
  ["click", "mousedown"],
  () => {
    console.log("hello!");
  }
);
```

This will add two event listeners to the element with class `my-element`, one for the `click` event and one for the `mousedown` event, both with the same listener callback function that logs "hello!" to the console.
