# Guide to Creating HTML Elements

To create a new HTML element, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Document.createElement()` to create a new element.
3. Set the inner HTML of the element to the desired string using `Element.innerHTML`.
4. Use `Element.firstElementChild` to return the element version of the string.

Here's an example function to create an element from a string, without appending it to the document:

```js
const createElement = (str) => {
  const el = document.createElement("div");
  el.innerHTML = str;
  return el.firstElementChild;
};
```

To use this function, pass the desired HTML string as an argument, like this:

```js
const el = createElement(
  `<div class="container">
    <p>Hello!</p>
  </div>`
);

console.log(el.className); // 'container'
```

Note that if the given string contains multiple elements, only the first one will be returned.
