# Responsive Layout With Sidebar

To create a responsive layout with a content area and a sidebar, follow these steps:

1. Write the code in `index.html` and `style.css`.
2. Use `display: grid` on the parent container to create a grid layout.
3. Use `minmax()` for the second column (sidebar) to allow it to take up between `150px` and `20%`.
4. Use `1fr` for the first column (main content) to take up the rest of the remaining space.

Here's an example code snippet:

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```
