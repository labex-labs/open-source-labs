# Bouncing Loader

This code block creates a bouncing loader animation in `index.html` and `style.css`. Follow these steps to create the animation:

1. Define a bouncing animation using the `opacity` and `transform` properties with `@keyframes`. Use a single axis translation on `transform: translate3d()` to achieve better animation performance.
2. Create a parent container, `.bouncing-loader`, for the bouncing circles. Use `display: flex` and `justify-content: center` to position them in the center.
3. Make the three bouncing circle `<div>` elements circular by giving them the same `width`, `height`, and `border-radius: 50%`.
4. Apply the `bouncing-loader` animation to each of the three bouncing circles.
5. Use a different `animation-delay` for each circle and `animation-direction: alternate` to create the appropriate effect.

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```