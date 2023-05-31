# How to Calculate Scrollbar Width in JavaScript

To calculate the width of the vertical scrollbar in JavaScript, follow these steps:

1. Use `Window.innerWidth` to get the interior width of the window.
2. Use `Element.clientWidth` to get the inner width of the `Document` element.
3. Subtract the `Element.clientWidth` from `Window.innerWidth` to get the width of the vertical scrollbar.

Here's the code to calculate the width of the vertical scrollbar:

```js
const getScrollbarWidth = () => {
  return window.innerWidth - document.documentElement.clientWidth;
};

getScrollbarWidth(); // 15
```

To start practicing coding, open the Terminal/SSH and type `node`.
