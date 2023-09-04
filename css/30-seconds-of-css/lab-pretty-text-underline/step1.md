# Pretty Text Underline

`index.html` and `style.css` have already been provided in the VM.

To avoid descenders clipping the underline, use `text-shadow` with four values to create a thick shadow that covers the line where descenders meet the underline. Ensure that the `text-shadow` color matches the `background` color and adjust the `px` values for larger fonts. Create the actual underline using `background-image` with a `linear-gradient()` and `currentColor`. Set `background-position`, `background-repeat`, and `background-size` to place the gradient in the correct position. Use the `::selection` pseudo-class selector to ensure that the text shadow does not interfere with text selection. Note that this effect is natively implemented as `text-decoration-skip-ink: auto`, but it has less control over the underline.

Here's an example code snippet:

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
