# Scroll Progress Bar

To create a progress bar that shows the scroll percentage of a page, follow these steps:

1. Add the following code to `index.html`:
```html
<div id="scroll-progress"></div>
```

2. Add the following code to `style.css`:
```css
body {
  min-height: 200vh;
}

#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

3. Use `EventTarget.addEventListener()` and `Element.scrollTop` to determine the scroll percentage of the document and apply it to the `width` of the element. Add the following JavaScript code to your project:
```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```