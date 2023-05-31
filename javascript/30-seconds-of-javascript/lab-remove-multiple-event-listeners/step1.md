# Detaching Event Listeners from Targets

To remove an event listener from multiple targets, use the `removeEventListenerAll()` function. This function takes in the targets, event type, listener, options, and useCapture as parameters. It uses `Array.prototype.forEach()` and `EventTarget.removeEventListener()` to detach the provided `listener` for the given event `type` from all `targets`.

Here's an example of how to use it:

```js
const linkListener = () => console.log("Clicked a link");
document.querySelector("a").addEventListener("click", linkListener);

// Detach the listener from all anchor tags
removeEventListenerAll(document.querySelectorAll("a"), "click", linkListener);
```

After calling the `removeEventListenerAll()` function, the `linkListener` will no longer be triggered when any of the anchor tags are clicked.
