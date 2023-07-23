# How to Hide Elements with JavaScript

To hide elements on a webpage using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the spread operator (`...`) and `Array.prototype.forEach()` to apply `display: none` to each element specified.
3. The code snippet below demonstrates how to hide all elements of a specified type (e.g. all `<img>` elements) on the page:

```js
const hide = (...el) => [...el].forEach((e) => (e.style.display = "none"));
hide(...document.querySelectorAll("img")); // Hides all <img> elements on the page
```
