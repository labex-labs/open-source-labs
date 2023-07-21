# Checking if an Element is Visible in the Viewport

To check if an element is visible in the viewport, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding practice.
2. Use `Element.getBoundingClientRect()`, `Window.innerWidth`, and `Window.innerHeight` to determine if the element is visible in the viewport.
3. Omit the second argument to determine if the element is entirely visible. Alternatively, specify `true` to determine if it is partially visible.

Here's a code snippet that you can use:

```js
const elementIsVisibleInViewport = (el, partiallyVisible = false) => {
  const { top, left, bottom, right } = el.getBoundingClientRect();
  const { innerHeight, innerWidth } = window;
  return partiallyVisible
    ? ((top > 0 && top < innerHeight) ||
        (bottom > 0 && bottom < innerHeight)) &&
        ((left > 0 && left < innerWidth) || (right > 0 && right < innerWidth))
    : top >= 0 && left >= 0 && bottom <= innerHeight && right <= innerWidth;
};
```

Here's how you can use the code snippet:

```js
// e.g. 100x100 viewport and a 10x10px element at position {top: -1, left: 0, bottom: 9, right: 10}
elementIsVisibleInViewport(el); // false - (not fully visible)
elementIsVisibleInViewport(el, true); // true - (partially visible)
```
