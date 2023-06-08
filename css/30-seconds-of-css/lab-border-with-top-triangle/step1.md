# Border With Top Triangle

`index.html` and `style.css` have already been provided in the VM.

To create a content container with a triangle at the top, follow these steps:

1. Use the `::before` and `::after` pseudo-elements to create two triangles.
2. Set the `border-color` and `background-color` of the triangles to match the container.
3. Set the `border-width` of the `::before` triangle to be `1px` wider than the `::after` triangle to act as the border.
4. Position the `::after` triangle `1px` to the right of the `::before` triangle to allow for the left border to be shown.

Here is an example HTML code for the container:
```html
<div class="container">Border with top triangle</div>
```

And here is the corresponding CSS code:
```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
