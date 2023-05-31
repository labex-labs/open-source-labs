# How to Add an Event Listener to an Element

To add an event listener to an element, follow these steps:

1. Use `EventTarget.addEventListener()` method.
2. If you want to use event delegation, provide a `target` property to the options object.
3. Ensure that the event target matches the specified target and invoke the callback by supplying the correct `this` context.
4. If you don't want to use delegation, omit `opts` to default to non-delegation behavior and event bubbling.
5. The function returns a reference to the custom delegator function, which can be used with the `off` method.

Here is an example implementation of the `on` function:

```js
const on = (el, evt, fn, opts = {}) => {
  const delegatorFn = (e) =>
    e.target.matches(opts.target) && fn.call(e.target, e);
  el.addEventListener(
    evt,
    opts.target ? delegatorFn : fn,
    opts.options || false
  );
  if (opts.target) return delegatorFn;
};
```

And here are some examples of how to use it:

```js
const fn = () => console.log("!");
on(document.body, "click", fn); // logs '!' upon clicking the body
on(document.body, "click", fn, { target: "p" });
// logs '!' upon clicking a `p` element child of the body
on(document.body, "click", fn, { options: true });
// use capturing instead of bubbling
```
