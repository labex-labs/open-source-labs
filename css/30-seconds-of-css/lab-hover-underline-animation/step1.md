# Hover Underline Animation

`index.html` and `style.css` have already been provided in the VM.

To create an animated underline effect when the user hovers over the text, follow these steps:

1. Use `display: inline-block` to make the underline span just the width of the text content.
2. Use the `::after` pseudo-element with `width: 100%` and `position: absolute` to place it below the content.
3. Use `transform: scaleX(0)` to initially hide the pseudo-element.
4. Use the `:hover` pseudo-class selector to apply `transform: scaleX(1)` and display the pseudo-element on hover.
5. Animate `transform` using `transform-origin: left` and an appropriate `transition`.
6. Remove the `transform-origin` property to make the transform originate from the center of the element.

Here is an example HTML code to apply the effect to a text element:

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

And here is the corresponding CSS code:

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
