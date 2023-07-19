# Bouncing Loader

`index.html` and `style.css` have already been provided in the VM.

To create a bouncing loader animation:

1. Define a `@keyframes` animation that uses the `opacity` and `transform` properties, with a single axis translation on `transform: translate3d()` for better performance.
2. Create a parent container with the class `.bouncing-loader` that uses `display: flex` and `justify-content: center` to center the bouncing circles.
3. Give the three `<div>` elements for the bouncing circles the same `width`, `height`, and `border-radius: 50%` to make them circular.
4. Apply the `bouncing-loader` animation to each of the three bouncing circles.
5. Use a different `animation-delay` for each circle and `animation-direction: alternate` to create the appropriate effect.

Here is the HTML code:

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

And here is the CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
