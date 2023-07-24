# Pulse Loader

`index.html` and `style.css` have already been provided in the VM.

To create a pulse effect loader animation using the `animation-delay` property, follow these steps:

1. Use `@keyframes` to define an animation for two `<div>` elements. Set the starting point (`0%`) for both elements to have no `width` or `height` and to be positioned at the center. For the ending point (`100%`), have both elements increase in `width` and `height`, but reset their `position` to `0`.
2. Use `opacity` to transition from `1` to `0` when animating to give the `<div>` elements a disappearing effect as they expand.
3. Set a predefined `width` and `height` for the parent container, `.ripple-loader`. Use `position: relative` to position its children.
4. Use `animation-delay` on the second `<div>` element, so that each element starts its animation at a different time.

Here is the HTML and CSS code to achieve this:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
