# Responsive Layout With Sidebar

`index.html` and `style.css` have already been provided in the VM.

To create a responsive layout with a content area and a sidebar, use `display: grid` on the parent container, `minmax()` for the second column (sidebar) to allow it to take up between `150px` and `20%`, and `1fr` for the first column (main content) to take up the rest of the remaining space. Here is an example HTML and CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
