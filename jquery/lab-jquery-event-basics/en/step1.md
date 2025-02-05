# Setting Up Event Responses on DOM Elements

> `index.html` have already been provided in the VM.

jQuery makes it straightforward to set up event-driven responses on page elements. These events are often triggered by the end user's interaction with the page, such as when text is entered into a form element or the mouse pointer is moved. In some cases, such as the page load and unload events, the browser itself will trigger the event.

jQuery offers convenience methods for most native browser events. These methods — including `.click()`, `.focus()`, `.blur()`, `.change()`, etc. — are shorthand for jQuery's `.on()` method. The on method is useful for binding the same handler function to multiple events, when you want to provide data to the event handler, when you are working with custom events, or when you want to pass an object of multiple events and handlers.

```js
// Event setup using a convenience method
$("p").click(function () {
  console.log("You clicked a paragraph!");
});
```

```js
// Equivalent event setup using the `.on()` method
$("p").on("click", function () {
  console.log("click");
});
```

> Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
