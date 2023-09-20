# Setting Up Multiple Event Responses

Quite often elements in your application will be bound to multiple events. If multiple events are to share the same handling function, you can provide the event types as a space-separated list to `.on()`:

```js
// Multiple events, same handler
$("div").on(
  "click change", // Bind handlers for multiple events
  function () {
    console.log("An input was clicked or changed!");
  }
);
```

When each event has its own handler, you can pass an object into `.on()` with one or more key/value pairs, with the key being the event name and the value being the function to handle the event.

```js
// Binding multiple events with different handlers
$("div").on({
  click: function () {
    console.log("clicked!");
  },
  mouseover: function () {
    console.log("hovered!");
  }
});
```

> You can refresh the HTTP 8080 Tab to preview the web page.
