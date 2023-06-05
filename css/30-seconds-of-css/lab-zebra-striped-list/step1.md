# Zebra Striped List

To create a striped list with alternating background colors, write the code in `index.html` and `style.css`. Use the `:nth-child(odd)` or `:nth-child(even)` pseudo-class selectors to apply a different `background-color` to elements based on their position in a group of siblings. Note that you can use this technique to apply different styles to other HTML elements like `<div>`, `<tr>`, `<p>`, `<ol>`, etc.

Here's an example code block:

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

To apply the alternating background colors, add the following code block to `style.css`:

```css
li:nth-child(odd) {
  background-color: #999;
}
```