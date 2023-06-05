# Ensuring Constant Width to Height Ratio

To ensure that an element with variable `width` has a proportionate `height` value, follow these steps:

1. Apply `padding-top` on the `::before` pseudo-element to make the `height` of the element equal to a percentage of its `width`.
2. Adjust the proportion of `height` to `width` as necessary. For example, a `padding-top` of `100%` will create a responsive square with a 1:1 ratio.
3. Write the following code in `index.html` and `style.css`:

```html
<div class="constant-width-to-height-ratio"></div>
```

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```
