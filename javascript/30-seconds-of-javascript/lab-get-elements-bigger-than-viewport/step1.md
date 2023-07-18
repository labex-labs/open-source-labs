# How to Retrieve HTML Elements Wider Than the Viewport

To retrieve an array of HTML elements that are wider than the viewport, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `HTMLElement.offsetWidth` to get the width of the `Document`.
3. Use `Document.querySelectorAll()` to get all elements in the document and `Array.prototype.filter()` to check the width of each element.
4. Return an array of elements whose width is larger than that of the viewport's.

Here's the JavaScript code:

```js
const getElementsBiggerThanViewport = () => {
  const docWidth = document.documentElement.offsetWidth;
  return [...document.querySelectorAll("*")].filter(
    (el) => el.offsetWidth > docWidth
  );
};
```

To test the function, call `getElementsBiggerThanViewport()` and it will return an array of HTML elements that are wider than the viewport. For example:

```js
getElementsBiggerThanViewport(); // <div id="ultra-wide-item" />
```

This code will help you quickly find elements wider than the viewport and adjust them accordingly.
