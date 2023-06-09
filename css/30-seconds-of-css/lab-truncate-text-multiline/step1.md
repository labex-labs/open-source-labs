# Truncate Multiline Text

`index.html` and `style.css` have already been provided in the VM.

To truncate text that is longer than one line, follow these steps:

1. Use `overflow: hidden` to prevent the text from overflowing its dimensions.
2. Set a fixed `width` of `400px` to ensure the element has at least one constant dimension.
3. Set `height: 109.2px` as calculated from the `font-size`, using the formula `font-size * line-height * numberOfLines` (in this case `26 * 1.4 * 3 = 109.2`).
4. Add the class `truncate-text-multiline` to the `p` element in your HTML.
5. Set `font-size: 26px` and `line-height: 1.4` in the CSS for the `.truncate-text-multiline` class.
6. Set `color: #333` and `background: #f5f6f9` to style the text.
7. To create a gradient from `transparent` to the `background-color`, add the following CSS rules to the `.truncate-text-multiline::after` pseudo-element:

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

This will create a gradient container with a height of `36.4px`, calculated for the gradient container, based on the formula `font-size * line-height` (in this case `26 * 1.4 = 36.4`). The `::after` pseudo-element is positioned at the bottom right corner of the `.truncate-text-multiline` element.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
