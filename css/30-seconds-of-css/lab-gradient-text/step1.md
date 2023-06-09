# Gradient Text

`index.html` and `style.css` have already been provided in the VM.

To give text a gradient color, you can use CSS properties. First, use the `background` property with a `linear-gradient()` value to give the text element a gradient background. Then, use `webkit-text-fill-color: transparent` to fill the text with a transparent color. Finally, use `webkit-background-clip: text` to clip the background with the text and fill the text with the gradient background as the color. Here's an example code snippet:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
