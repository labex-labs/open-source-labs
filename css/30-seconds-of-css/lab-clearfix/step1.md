# Clearfix

To ensure that an element clears its children, use the following steps:

- Add the `::after` pseudo-element to the element you want to clear.
- Apply `content: ''` to the `::after` pseudo-element to allow it to affect layout.
- Use `clear: both` to make the element clear past both left and right floats.
- To avoid any issues, ensure that there are no non-floating children in the container and that there are no tall floats before the clearfixed container but in the same formatting context (e.g. floated columns).
- Note that this technique is only useful if you are using `float` to build layouts. Consider using a more modern approach, such as the flexbox or grid layout.

Example HTML code:

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

Example CSS code:

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```
