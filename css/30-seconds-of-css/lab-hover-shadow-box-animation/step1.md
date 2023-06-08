# Hover Shadow Box Animation

This code creates a shadow box around the text when it is hovered. To implement this, follow these steps:

1. In the `style.css` file, set the `transform` property of the `.hover-shadow-box-animation` class to `perspective(1px) translateZ(0)`. This creates a 3D space effect and repositions the `p` element along the z-axis.
2. Use the `box-shadow` property to make the box transparent.
3. Use the `transition-property` property to enable transitions for both `box-shadow` and `transform`.
4. Use the `:hover`, `:active`, and `:focus` pseudo-class selectors to apply a new `box-shadow` and `transform: scale(1.2)` to change the scale of the text.

To use the code, add the following `html` code to your `index.html` file:

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

And add the following `css` code to your `style.css` file:

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition-duration: 0.3s;
  transition-property: box-shadow, transform;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```
