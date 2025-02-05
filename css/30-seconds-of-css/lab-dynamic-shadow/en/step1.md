# Dynamic Shadow

`index.html` and `style.css` have already been provided in the VM.

To create a shadow that is based on the colors of an element, follow these steps:

1. Use the `::after` pseudo-element with `position: absolute` and `width` and `height` set to `100%` to fill the available space in the parent element.

2. Inherit the `background` of the parent element by using `background: inherit`.

3. Slightly offset the pseudo-element using `top`. Then, use `filter: blur()` to create a shadow, and set `opacity` to make it semi-transparent.

4. Position the pseudo-element behind its parent by setting `z-index: -1`. Set `z-index: 1` on the parent element.

Here's an example HTML and CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
