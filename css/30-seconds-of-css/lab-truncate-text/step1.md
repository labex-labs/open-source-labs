# Truncate Text

To truncate text that is longer than one line and add an ellipsis at the end (`…`), use the following steps:

- Apply `overflow: hidden` to prevent the text from overflowing its dimensions.
- Use `white-space: nowrap` to prevent the text from exceeding one line in height.
- Use `text-overflow: ellipsis` to end the text with an ellipsis if it exceeds its dimensions.
- Specify a fixed `width` for the element to know when to display an ellipsis.
- Note that this method only works for single line elements.

Example usage:

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```
