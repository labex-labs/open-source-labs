# How to Remove a DOM Element in JavaScript

To remove an element from the DOM using JavaScript, you can follow these steps:

1. Get the parent node of the element using `Node.parentNode`.
2. Use `Node.removeChild()` method to remove the element from its parent node.

Here's an example code snippet that demonstrates how to remove a DOM element:

```js
const removeElement = (el) => el.parentNode.removeChild(el);
```

You can call this function with the element you want to remove as an argument. For example, to remove an element with the ID `my-element`, you can use the following code:

```js
removeElement(document.querySelector("#my-element"));
// This will remove #my-element from the DOM
```
