# Events

> `index.html` have already been provided in the VM.

Real interactivity on a website requires event handlers. These are code structures that listen for activity in the browser, and run code in response. The most obvious example is handling the [click event](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), which is fired by the browser when you click on something with your mouse. To demonstrate this, enter the following into your console, then click on the current webpage:

```js
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

There are a number of ways to attach an event handler to an element.
Here we select the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html) element. We then call its [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) function, passing in the name of the event to listen to (`'click'`) and a function to run when the event happens.

The function we just passed to `addEventListener()` here is called an _anonymous function_, because it doesn't have a name. There's an alternative way of writing anonymous functions, which we call an _arrow function_.
An arrow function uses `() =>` instead of `function ()`:

```js
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

> Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
