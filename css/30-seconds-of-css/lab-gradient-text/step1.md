# Gradient Text

To give text a gradient color, follow these steps:

1. Write the code in `index.html` and `style.css`.
2. Use `background` with a `linear-gradient()` value to give the text element a gradient background.
3. Use `webkit-text-fill-color: transparent` to fill the text with a transparent color.
4. Use `webkit-background-clip: text` to clip the background with the text, filling the text with the gradient background as the color.

Here's an example code block:

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```
