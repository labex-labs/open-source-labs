# Grid Centering

`index.html` and `style.css` have already been provided in the VM.

To center a child element both horizontally and vertically within a parent element, follow these steps:

1. Create a grid layout using `display: grid`.
2. Use `justify-content: center` to center the child horizontally.
3. Use `align-items: center` to center the child vertically.

Here's an example HTML structure:

```html
<div class="parent">
  <div class="child">Centered content.</div>
</div>
```

And the corresponding CSS:

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
