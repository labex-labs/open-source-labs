# Etched Text

To create an "etched" or engraved effect on text:

- Open `index.html` and `style.css`.
- Use `text-shadow` with a white shadow offset `0px` horizontally and `2px` vertically from the origin position.
- The background should be darker than the shadow.
- Slightly fade the text color to make it appear carved out of the background.

Example code:

```html
<p class="etched-text">I appear etched into the background.</p>
```

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```
