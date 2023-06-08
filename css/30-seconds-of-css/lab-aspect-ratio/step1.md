# Aspect Ratio

`index.html` and `style.css` have already been provided in the VM.

Here's a revised version of the content:

---

This code creates a responsive container with a specific aspect ratio using CSS custom properties and `calc()` function. Follow these steps to achieve this:

1. Define the desired aspect ratio using a CSS custom property, `--aspect-ratio`.
2. Set the container element's `position` property to `relative` and its `height` property to `0`.
3. Calculate the container element's height using the `calc()` function and the `--aspect-ratio` custom property, and set it as the `padding-bottom` property.
4. Set the direct child of the container element to `position: absolute`, `top: 0`, `left: 0`, `width: 100%`, and `height: 100%`.
5. Maintain the aspect ratio of the child element by setting its `object-fit` property to `cover`.

Use the following HTML and CSS code to create the container:

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
