# Scroll Progress Bar

`index.html` and `style.css` have already been provided in the VM.

To create a progress bar that shows the scroll percentage of a webpage, follow these steps:

1. Add a `div` element with the `id` "scroll-progress" to the HTML code.
2. In the CSS code, set the `position` of the element to `fixed`, the `top` to `0`, the `width` to `0%`, the `height` to `4px`, and the `background` color to `#7983ff`.
3. Set the `z-index` value to a large number to ensure that the progress bar is placed at the top of the page and above any content.
4. In the JavaScript code, select the `scroll-progress` element using the `document.getElementById()` method.
5. Calculate the height of the webpage using the formula `document.documentElement.scrollHeight - document.documentElement.clientHeight`.
6. Add an event listener to the `window` object that listens for the `scroll` event.
7. In the event listener function, calculate the scroll percentage of the document using the formula `(scrollTop / height) * 100`.
8. Set the `width` of the `scroll-progress` element to the scroll percentage using the `style` property.

Here is the revised code:

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
