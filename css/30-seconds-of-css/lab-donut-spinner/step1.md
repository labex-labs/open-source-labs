# Donut Spinner

`index.html` and `style.css` have already been provided in the VM.

To indicate the loading of content, create a donut spinner with a semi-transparent `border` for the whole element. Exclude one side to serve as the loading indicator for the donut. Then, define and use an appropriate animation, using `transform: rotate()` to rotate the element. Here's an example code in HTML and CSS:

HTML:
```html
<div class="donut"></div>
```

CSS:
```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
