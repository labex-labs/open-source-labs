# Zoom in Zoom Out Animation

`index.html` and `style.css` have already been provided in the VM.

To create a zoom in zoom out animation, follow these steps:

1. Define a three-step animation using `@keyframes`. At `0%` and `100%`, set the element to its original size using `scale(1,1)`. At `50%`, scale it up to 1.5 times its original size using `scale(1.5,1.5)`.

2. Give the element a specific size using `width` and `height`.

3. Use `animation` to set the appropriate values for the element to make it animated.

Here's an example HTML and CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
