# Shape Separator

`index.html` and `style.css` have already been provided in the VM.

To create a separator element between two different blocks using an SVG shape, follow these steps:

1. Use the `::after` pseudo-element.
2. Add the SVG shape (a 24x12 triangle) via a data URI using the `background-image` property. The background image will repeat by default and cover the whole area of the pseudo-element.
3. Set the desired color for the separator by using the `background` property of the parent element.

Use the following HTML code:
```html
<div class="shape-separator"></div>
```

And apply the following CSS rules:
```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9C27B0;
}

.shape-separator::after {
  content: '';
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
