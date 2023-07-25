# How to Check if the Bottom of the Page Is Visible

To check if the bottom of the page is visible, you can use the following code:

```js
const bottomVisible = () =>
  document.documentElement.clientHeight + window.scrollY >=
  (document.documentElement.scrollHeight ||
    document.documentElement.clientHeight);
```

To use this code, open the Terminal/SSH and type `node`. Then, use `Window.scrollY`, `Element.scrollHeight`, and `Element.clientHeight` to determine if the bottom of the page is visible.

You can test the function by calling `bottomVisible()`, which will return `true` if the bottom of the page is visible.
