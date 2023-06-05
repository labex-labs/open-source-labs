# Offscreen

To hide an element completely in the DOM while still allowing it to be accessible, use the following steps:
- Remove all borders, padding, and overflow of the element.
- Use `clip` to define that no part of the element is shown.
- Set the `height` and `width` of the element to `1px` and negate them using `margin: -1px`.
- Use `position: absolute` to prevent the element from taking up space in the DOM.

Note that this technique is a better alternative to `display: none` (not readable by screen readers) and `visibility: hidden` (takes up physical space in the DOM).

Here is an example code in `index.html` and `style.css`:

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