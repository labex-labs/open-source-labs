# Function to Remove Attributes

To remove all attributes from an HTML element, you can use the following function:

```js
const removeAttributes = (element) => {
  Object.values(element.attributes).forEach(({ name }) => {
    element.removeAttribute(name);
  });
};
```

To use this function, simply pass the element you want to modify as an argument. For example:

```js
removeAttributes(document.querySelector("p.special"));
```

This will remove all attributes from the `p` element with the class `special`.
