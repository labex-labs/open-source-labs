# Mouse Cursor Gradient Tracking

To create a hover effect where the gradient follows the mouse cursor, follow these steps:

1. In your `style.css` file, declare two CSS variables, `--x` and `--y`, that will be used to track the position of the mouse on the button.
2. Declare a CSS variable, `--size`, that will be used to modify the gradient's dimensions.
3. To create the gradient at the correct position, use the `background: radial-gradient(circle closest-side, pink, transparent)` property.
4. To register a handler for the `'mousemove'` event, use `Document.querySelector()` and `EventTarget.addEventListener()`.
5. To update the values of the `--x` and `--y` CSS variables, use `Element.getBoundingClientRect()` and `CSSStyleDeclaration.setProperty()`.

Here's an example of the HTML code you can use:

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

And here's an example of the corresponding CSS code:

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition: width 0.2s ease, height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Finally, here's an example of the JavaScript code you can use:

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```