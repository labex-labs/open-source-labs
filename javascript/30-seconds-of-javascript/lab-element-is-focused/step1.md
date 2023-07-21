# Checking if an Element is Focused

To check if an element is focused, use the `Document.activeElement` property.

```js
const elementIsFocused = (el) => el === document.activeElement;
```

Call the `elementIsFocused` function with the element you want to check as an argument. It will return `true` if the element is focused.

Example:

```js
elementIsFocused(el); // true
```
