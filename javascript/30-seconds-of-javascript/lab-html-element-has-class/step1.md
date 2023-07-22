# How to Check if an HTML Element Has a Class

To check if a specific HTML element has a certain class, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Element.classList` and `DOMTokenList.contains()` to check if the element has the specified class.
3. Implement the following function in your code:

```js
const hasClass = (el, className) => el.classList.contains(className);
```

4. Use the `hasClass()` function to check if the element has the class you're looking for. For example:

```js
hasClass(document.querySelector("p.special"), "special"); // returns true
```

By following these steps, you can easily check if an HTML element has a specific class in your code.
