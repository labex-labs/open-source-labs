# How to Add a Class to an HTML Element

To add a class to an HTML element, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Element.classList` and `DOMTokenList.add()` to add the specified class to the element.
3. Call the `addClass` function with the `el` parameter as the HTML element you want to add the class to and `className` parameter as the name of the class you want to add.

Here's an example of the `addClass` function:

```js
const addClass = (el, className) => el.classList.add(className);
```

To use the function, simply call it with the appropriate parameters:

```js
addClass(document.querySelector("p"), "special");
```

After running this code, the paragraph will now have the 'special' class.
