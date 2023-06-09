# Truncate Text

`index.html` and `style.css` have already been provided in the VM.

To truncate text that is longer than one line and add an ellipsis at the end, use the following CSS properties:

- `overflow: hidden` to prevent text from overflowing its dimensions
- `white-space: nowrap` to prevent text from exceeding one line in height
- `text-overflow: ellipsis` to add an ellipsis if text exceeds its dimensions
- Specify a fixed `width` for the element to know when to display an ellipsis

Note that this method only works for single line elements. For example:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
