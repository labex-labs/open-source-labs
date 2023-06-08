# Donut Spinner

This code creates a donut spinner that can be used to indicate the loading of content. To create the spinner:

- Write the code in `index.html` and `style.css`.
- Use a semi-transparent `border` for the whole element, except for one side that serves as the loading indicator for the donut.
- Define and use an appropriate animation, using `transform: rotate()` to rotate the element.

```html
<div class="donut"></div>
```

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
