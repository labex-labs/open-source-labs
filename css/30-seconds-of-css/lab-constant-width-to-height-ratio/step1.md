# Constant Width to Height Ratio

`index.html` and `style.css` have already been provided in the VM.

This code snippet ensures that an element with variable `width` will retain a proportionate `height` value. To achieve this, apply `padding-top` on the `::before` pseudo-element, making the `height` of the element equal to a percentage of its `width`. The proportion of `height` to `width` can be altered as necessary. For example, a `padding-top` of `100%` will create a responsive square with a 1:1 ratio. To use this code, simply add the following HTML code:

```html
<div class="constant-width-to-height-ratio"></div>
```

Then, add the following CSS code:

```css
.constant-width-to-height-ratio {
  background: #9C27B0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: '';
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: '';
  display: block;
  clear: both;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
