# Code for Vertically and Horizontally Centering a Child Element

To center a child element both horizontally and vertically within its parent element, use the following HTML and CSS code:

```html
<div class="container">
  <div class="center"><span>Centered content</span></div>
</div>
```

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}

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

To achieve this result, follow these steps:

1. Add a parent element with a fixed `height` and `width`. In this example, the parent element is `.container`.
2. Add a child element with the class `.center`.
3. Use `display: table` to make the `.center` element behave like a `<table>` element.
4. Set `height` and `width` to `100%` to make the element fill the available space within its parent element.
5. Use `display: table-cell` on the child element to make it behave like a `<td>` elements.
6. Use `text-align: center` and `vertical-align: middle` on the child element to center it horizontally and vertically.