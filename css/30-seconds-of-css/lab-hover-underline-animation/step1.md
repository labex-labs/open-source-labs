# Animated Underline Effect on Hover

This code creates an animated underline effect when the user hovers over the text. To implement it, follow the instructions below:

1. Add the following HTML code to `index.html`:

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

2. Add the following CSS code to `style.css`:

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
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transform: scaleX(0);
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

The CSS code above uses the following properties:

- `display: inline-block` to make the underline span just the width of the text content.
- `position: relative` to establish the containing block for the `::after` pseudo-element.
- `color: #0087ca` to set the text color.
- `::after` pseudo-element with `width: 100%` and `position: absolute` to place it below the content.
- `transform-origin: bottom right` to set the origin of the scaling transformation to the bottom right corner of the element.
- `transform: scaleX(0)` to initially hide the pseudo-element.
- `transition: transform 0.25s ease-out` to animate the transformation over a duration of 0.25 seconds.
- `:hover` pseudo-class selector to apply `transform: scaleX(1)` and display the pseudo-element on hover.
- `transform-origin: bottom left` to set the origin of the scaling transformation to the bottom left corner of the element.

You can modify the CSS properties to customize the animation to your liking.