# Offscreen

`index.html` and `style.css` have already been provided in the VM.

This technique completely hides an element in the DOM while still making it accessible. To achieve this, you can follow these steps:
- Remove all borders and padding and hide the element's overflow.
- Use `clip` to ensure that no part of the element is shown.
- Set the `height` and `width` of the element to `1px` and negate them using `margin: -1px`.
- Use `position: absolute` to prevent the element from taking up space in the DOM.
- Note that this technique is a better alternative to `display: none` (not readable by screen readers) and `visibility: hidden` (takes up physical space in the DOM) in terms of accessibility and layout-friendliness.

Here's an example of how you can use this technique in HTML and CSS:

```html
<a class="button" href="https://google.com">
  Learn More <span class="offscreen">about pants</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
