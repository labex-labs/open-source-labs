# Event Hub Creation

To create an event hub with `emit`, `on`, and `off` methods, follow the steps:

1. Use `Object.create(null)` to create an empty `hub` object that does not inherit properties from `Object.prototype`.
2. For `emit`, resolve the array of handlers based on the `event` argument and then run each one with `Array.prototype.forEach()` by passing in the data as an argument.
3. For `on`, create an array for the event if it does not yet exist, then use `Array.prototype.push()` to add the handler to the array.
4. For `off`, use `Array.prototype.findIndex()` to find the index of the handler in the event array and remove it using `Array.prototype.splice()`.

Here's the code:

```js
const createEventHub = () => ({
  hub: Object.create(null),
  emit(event, data) {
    (this.hub[event] || []).forEach((handler) => handler(data));
  },
  on(event, handler) {
    if (!this.hub[event]) this.hub[event] = [];
    this.hub[event].push(handler);
  },
  off(event, handler) {
    const i = (this.hub[event] || []).findIndex((h) => h === handler);
    if (i > -1) this.hub[event].splice(i, 1);
    if (this.hub[event].length === 0) delete this.hub[event];
  },
});
```

To use the event hub:

1. Subscribe to events by listening for different types of events using `on()`.
2. Publish events to invoke all handlers subscribed to them, passing the data to them as an argument using `emit()`.
3. Unsubscribe to an event by stopping a specific handler from listening to the event using `off()`.

Here's an example:

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// Subscribe: listen for different types of events
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// Publish: emit events to invoke all handlers subscribed to them, passing the data to them as an argument
hub.emit("message", "hello world"); // logs 'hello world' and 'Message event fired'
hub.emit("message", { hello: "world" }); // logs the object and 'Message event fired'
hub.emit("increment"); // `increment` variable is now 1

// Unsubscribe: stop a specific handler from listening to the 'message' event
hub.off("message", handler);
```
