# Image Text Overlay

`index.html` and `style.css` have already been provided in the VM.

To display text on top of an image with an overlay, use the `backdrop-filter` property to apply a `blur(14px)` and `brightness(80%)` effect. This ensures that the text is readable regardless of the background image and color. Here is an example HTML code:

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800">
</div>
```

And the corresponding CSS code:

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
