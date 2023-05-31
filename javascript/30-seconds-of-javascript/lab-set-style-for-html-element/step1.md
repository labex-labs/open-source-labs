# Here's a revised version of the given sentences:

To set the value of a CSS rule for a specific HTML element, use `HTMLElement.style` and specify the rule and value. For example, you can use the following function to set the style of an element:

```js
const setStyle = (element, rule, value) => (element.style[rule] = value);
```

To apply this function to a specific element, use `document.querySelector` to select the element and then call `setStyle` with the desired rule and value as arguments. For instance, `setStyle(document.querySelector('p'), 'font-size', '20px')` will set the font size of the first `<p>` element on the page to 20 pixels.

If you want to practice coding, you can open the Terminal/SSH and type `node`.
