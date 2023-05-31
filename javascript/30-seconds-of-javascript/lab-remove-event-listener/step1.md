# How to Remove Event Listener From Element

To remove an event listener from an element, use `EventTarget.removeEventListener()`. You can omit the fourth argument `opts` to use `false` or specify it based on the options used when the event listener was added. Here's an example function:

```js
const off = (el, evt, fn, opts = false) =>
  el.removeEventListener(evt, fn, opts);
```

To use the function, first define the event listener with `addEventListener` and then call `off` with the same arguments to remove it. For example:

```js
const fn = () => console.log("!");
document.body.addEventListener("click", fn);
off(document.body, "click", fn); // no longer logs '!' upon clicking on the page
```

To start practicing coding, open the Terminal/SSH and type `node`.
