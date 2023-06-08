# Zebra Striped List

`index.html` and `style.css` have already been provided in the VM.

To create a list with alternating background colors, use the `:nth-child(odd)` or `:nth-child(even)` pseudo-class selectors to apply a different `background-color` to elements based on their position among siblings. This can be applied to various HTML elements such as `<div>`, `<tr>`, `<p>`, `<ol>`, etc. 

Here's an example of how to create a striped list with `<li>` elements:

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
