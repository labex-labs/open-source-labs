# Aspect Ratio

To create a responsive container with a specific aspect ratio, follow these steps:

1. Define the desired aspect ratio using the CSS custom property `--aspect-ratio`.
2. Set the container element to `position: relative` and `height: 0`.
3. Use the `calc()` function and the `--aspect-ratio` custom property to calculate the container element's height.
4. Set the direct child of the container element to `position: absolute`, `width: 100%`, `height: 100%`, and `object-fit: cover`.

Here is an example code block to help you get started:

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