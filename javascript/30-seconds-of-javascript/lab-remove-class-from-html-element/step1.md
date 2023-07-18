# How to Remove a Class from an HTML Element using JavaScript

To remove a class from an HTML element using JavaScript, follow these steps:

1. Use the `Element.classList` property to access the class list of the element.
2. Call the `DOMTokenList.remove()` method on the class list, passing the name of the class to remove as an argument.

Here's an example function that removes a class from an element:

```js
const removeClass = (el, className) => el.classList.remove(className);
```

To use this function, pass in the element you want to modify and the name of the class you want to remove:

```js
removeClass(document.querySelector("p.special"), "special");
```

After running this code, the `p.special` element will no longer have the `special` class.
