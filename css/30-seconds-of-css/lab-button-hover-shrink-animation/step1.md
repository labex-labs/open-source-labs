# Button Shrink Animation

This code creates a shrink animation on hover for a button element. The code is written in `index.html` and `style.css`.

To animate changes to the button, an appropriate `transition` is used. When the user hovers over the button, the `transform` property is changed to `scale(0.8)`, shrinking the element.

```html
<button class="button-shrink">Submit</button>
```

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```
