# Display Table Centering

`index.html` and `style.css` have already been provided in the VM.

To center a child element both vertically and horizontally within its parent element, follow these steps:

1. Add a container element with a fixed `height` and `width`.
```html
<div class="container">
```

2. Add the child element inside the container element and give it a class of `.center`.
```html
  <div class="center"><span>Centered content</span></div>
</div>
```

3. In the CSS, apply the following styles to the container element:
  - Set `height` and `width` to the desired fixed values.
  - Add a border (optional).
```css
.container {
  border: 1px solid #9C27B0;
  height: 250px;
  width: 250px;
}
```

4. In the CSS, apply the following styles to the child element:
  - Use `display: table` to make the `.center` element behave like a `<table>` element.
  - Set `height` and `width` to `100%` to make the element fill the available space within its parent element.
  - Use `display: table-cell` on the child element to make it behave like a `<td>` element.
  - Use `text-align: center` and `vertical-align: middle` on the child element to center it horizontally and vertically.
```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
