# Attaching an Event Listener to Multiple Targets

To add an event listener to multiple targets, use the `addEventListenerAll` function. This function uses `Array.prototype.forEach()` and `EventTarget.addEventListener()` to attach the provided `listener` for the given event `type` to all `targets`.

```js
const addEventListenerAll = (targets, type, listener, options, useCapture) => {
  targets.forEach((target) =>
    target.addEventListener(type, listener, options, useCapture)
  );
};
```

To use this function, pass in an array of `targets`, the `type` of event to listen for, the `listener` function to execute when the event is triggered, and any optional `options` and `useCapture` arguments. For example:

```js
addEventListenerAll(document.querySelectorAll("a"), "click", () =>
  console.log("Clicked a link")
);
// Logs 'Clicked a link' whenever any anchor element is clicked
```

To start practicing coding, open the Terminal/SSH and type `node`.
