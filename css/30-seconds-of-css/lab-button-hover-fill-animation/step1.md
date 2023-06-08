# Button Fill Animation

To create a fill animation on hover, follow these steps:

1. In `index.html` and `style.css`, set a `color` and `background` for the button.
2. Use an appropriate `transition` to animate changes to the button element.
3. Use the `:hover` pseudo-class to change the `background` and `color` of the button when the user hovers over it.
4. Add the class `animated-fill-button` to the `button` element in `index.html`.

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```
