# Extending Events to New Page Elements

It is important to note that `.on()` can only create event listeners on elements that exist at the time you set up the listeners.For example:

```js
$(document).ready(function () {
  // Now create a new button element with the alert class.
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // Sets up click behavior on all button elements with the alert class
  // that exist in the DOM when the instruction was executed
  $("button.alert").on("click", function () {
    console.log("A button with the alert class was clicked!");
  });
});
```

If similar elements are created after the event listeners are set up, they won't automatically pick up the event behaviors you've previously set up.

> You can refresh the **Web 8080** Tab to preview the web page.
