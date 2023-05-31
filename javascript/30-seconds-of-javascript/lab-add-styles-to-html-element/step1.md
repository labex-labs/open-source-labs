# How to Add Styles to an HTML Element in JavaScript

To add styles to an HTML element using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.assign()` and `HTMLElement.style` to merge the provided `styles` object into the style of the given element.
3. Use the `addStyles` function, which takes two arguments: the HTML element and an object containing the styles you want to add.

Here's an example of how to use the `addStyles` function:

```js
const addStyles = (el, styles) => Object.assign(el.style, styles);

addStyles(document.getElementById("my-element"), {
  background: "red",
  color: "#ffff00",
  fontSize: "3rem",
});
```

This code will add the provided styles to the HTML element with the ID `my-element`. You can modify the styles object to suit your needs.
