# Retrieving CSS Rule Value for Element

To retrieve the value of a CSS rule for a specific element, use the `Window.getComputedStyle()` method. Here's an example of how to create a `getStyle` function that takes an element and a rule name as arguments and returns the corresponding CSS rule value:

```js
const getStyle = (el, ruleName) => getComputedStyle(el)[ruleName];
```

You can then use this function to retrieve the value of any CSS rule for a given element. For example:

```js
getStyle(document.querySelector("p"), "font-size"); // returns '16px'
```

To get started with coding practice, open the Terminal/SSH and type `node`.
