# Mouse Cursor Gradient Tracking

`index.html` and `style.css` have already been provided in the VM.

To create a hover effect where the gradient follows the mouse cursor, follow these steps:

1. Declare two CSS variables, `--x` and `--y`, to track the position of the mouse on the button.
2. Declare a CSS variable, `--size`, to modify the gradient's dimensions.
3. Use `background: radial-gradient(circle closest-side, pink, transparent)` to create the gradient at the correct position.
4. Register a handler for the `'mousemove'` event using `Document.querySelector()` and `EventTarget.addEventListener()`.
5. Update the values of the `--x` and `--y` CSS variables using `Element.getBoundingClientRect()` and `CSSStyleDeclaration.setProperty()`.

Here is the HTML code for the button:

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

And here is the CSS code:

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
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Finally, here is the JavaScript code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
