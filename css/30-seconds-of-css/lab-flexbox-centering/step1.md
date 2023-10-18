# Flexbox Centering

`index.html` and `style.css` have already been provided in the VM.

To center a child element both horizontally and vertically within a parent element using flexbox, follow these steps:

1. Create a flexbox layout by setting the parent element's `display` property to `flex`.
2. Use the `justify-content` property to center the child horizontally by setting its value to `center`.
3. Use the `align-items` property to center the child vertically by setting its value to `center`.
4. Add the child element within the parent element.

Here's an example code snippet:

```html
<div class="flexbox-centering">
  <div>Centered content.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
