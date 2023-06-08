# How to create a zoom in zoom out animation

To create a zoom in zoom out animation, follow these steps:

1. Open the `index.html` and `style.css` files.
2. Define a three-step animation using `@keyframes`. At `0%` and `100%`, the element should be its original size (`scale(1 ,1)`). At `50%`, it should be scaled up to 1.5 times its original size (`scale(1.5, 1.5)`).
3. Use `width` and `height` to set the size of the element.
4. Apply the animation to the element using `animation` with the appropriate values.

Here is an example code block:

```html
<div class="zoom-in-out-box"></div>
```

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}

@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

This will create a box with a zoom in zoom out animation.
