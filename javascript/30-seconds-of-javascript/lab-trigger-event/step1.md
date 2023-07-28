# How to Trigger an Event on an HTML Element

To trigger an event on a specific element in HTML, follow these steps:

1. Open the Terminal/SSH to start coding practice.
2. Create a new event using the `CustomEvent` constructor and specify the `eventType` and details.
3. Use `EventTarget.dispatchEvent()` to trigger the new event on the element.
4. To pass custom data to the event, include the `detail` argument.

Here's an example of how to trigger an event on an HTML element:

```js
const triggerEvent = (el, eventType, detail) =>
  el.dispatchEvent(new CustomEvent(eventType, { detail }));
```

To trigger a click event on an element with the ID `myId`, use the following code:

```js
triggerEvent(document.getElementById("myId"), "click");
```

To pass custom data to the event, include it as an object in the `detail` argument:

```js
triggerEvent(document.getElementById("myId"), "click", { username: "bob" });
```
