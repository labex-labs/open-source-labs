# Grid Centering

To horizontally and vertically center a child element within a parent element using `grid`, follow these steps:

1. Write the code in `index.html` and `style.css`.
2. Use `display: grid` to create a grid layout.
3. Use `justify-content: center` to center the child horizontally.
4. Use `align-items: center` to center the child vertically.

Here's an example code block:

```html
<div class="grid-centering">
  <div class="child">Centered content.</div>
</div>
```

```css
.grid-centering {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```