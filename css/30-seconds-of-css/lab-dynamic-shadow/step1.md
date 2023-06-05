# Dynamic Shadow

To create a dynamic shadow based on the element's own colors, follow these steps:

1. Write the code in `index.html` and `style.css`.
2. Use the `::after` pseudo-element with `position: absolute` and `width` and `height` equal to `100%` to fill the available space in the parent element.
3. Use `background: inherit` to inherit the `background` of the parent element.
4. Slightly offset the pseudo-element with `top`, create a shadow with `filter: blur()`, and make it semi-transparent with `opacity`.
5. Position the parent element above the pseudo-element with `z-index: 1` on the parent and `z-index: -1` on the pseudo-element.

Here is an example code block:

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```
