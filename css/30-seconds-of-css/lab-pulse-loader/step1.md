# Pulse Loader

To create a pulse effect loader animation using the `animation-delay` property, follow these steps:

1. Define an animation at two points in the cycle using `@keyframes`. At `0%`, both `<div>` elements should be positioned at the center with no `width` or `height`. At `100%`, both elements should have increased `width` and `height`, but their `position` should be reset to `0`.
2. Use `opacity` to transition from `1` to `0` when animating to give the `<div>` elements a disappearing effect as they expand.
3. Set a predefined `width` and `height` for the parent container, `.ripple-loader`, and use `position: relative` to position its children.
4. Use `animation-delay` on the second `<div>` element so that each element starts its animation at a different time.

Here's the code for the HTML and CSS:

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```
