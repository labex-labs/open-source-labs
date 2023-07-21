# How to Render a DOM Element

To render a DOM tree in a specified DOM element, follow these steps:

1. Destructure the first argument into `type` and `props`. Use `type` to determine if the given element is a text element.
2. Based on the element's `type`, create the DOM element using either `Document.createTextNode()` or `Document.createElement()`.
3. Add attributes to the DOM element and set event listeners as necessary using `Object.keys()`.
4. Use recursion to render `props.children`, if any.
5. Finally, append the DOM element to the specified `container` using `Node.appendChild()`.

Here is the code:

```js
const renderElement = ({ type, props = {} }, container) => {
  const isTextElement = !type;
  const element = isTextElement
    ? document.createTextNode("")
    : document.createElement(type);

  const isListener = (p) => p.startsWith("on");
  const isAttribute = (p) => !isListener(p) && p !== "children";

  Object.keys(props).forEach((p) => {
    if (isAttribute(p)) element[p] = props[p];
    if (!isTextElement && isListener(p))
      element.addEventListener(p.toLowerCase().slice(2), props[p]);
  });

  if (!isTextElement && props.children && props.children.length)
    props.children.forEach((childElement) =>
      renderElement(childElement, element)
    );

  container.appendChild(element);
};
```

To render an example element, create an object with the element's `type` and `props`. Then call `renderElement()` with the example object and the container where the element should be rendered:

```js
const myElement = {
  type: "button",
  props: {
    type: "button",
    className: "btn",
    onClick: () => alert("Clicked"),
    children: [{ props: { nodeValue: "Click me" } }],
  },
};

renderElement(myElement, document.body);
```
