# How to Listen for an Event Only Once

To add an event listener to an element that only runs the callback function the first time the event is triggered, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `EventTarget.addEventListener()` to add an event listener to the element.
3. Set `{ once: true }` as the options to only run the given callback function once.

```js
const listenOnce = (el, evt, fn) =>
  el.addEventListener(evt, fn, { once: true });
```

For example, to log "Hello world" only on the first click of an element with the ID "my-id", use the following code:

```js
listenOnce(document.getElementById("my-id"), "click", () =>
  console.log("Hello world")
); // 'Hello world' will only be logged on the first click
```
