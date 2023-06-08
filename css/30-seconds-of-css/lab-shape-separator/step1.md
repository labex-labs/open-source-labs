# Shape Separator

This code creates a separator between two blocks using an SVG shape.

To use it, add the following HTML:

```html
<div class="shape-separator"></div>
```

Then, add the following CSS rules:

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

These rules create a pseudo-element using `::after`, which displays the SVG shape as a background image. The background color can be changed by modifying the `background` property of the parent element.
