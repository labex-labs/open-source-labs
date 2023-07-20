# How to Toggle a Class for an HTML Element

To toggle a class for an HTML element, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Element.classList` and `DOMTokenList.toggle()` to toggle the specified class for the element.
3. To implement this, you can use the following code:

```js
const toggleClass = (el, className) => el.classList.toggle(className);
```

4. To test the code, use the following example:

```js
toggleClass(document.querySelector("p.special"), "special");
// The paragraph will not have the 'special' class anymore
```
