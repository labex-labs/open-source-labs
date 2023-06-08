# Clearfix

`index.html` and `style.css` have already been provided in the VM.

To ensure that an element self-clears its children when using `float` to build layouts, you can use the `::after` pseudo-element and apply `content: ''` to allow it to affect layout. Additionally, use `clear: both` to make the element clear past both left and right floats. However, this technique only works properly if there are no non-floating children in the container and there are no tall floats before the clearfixed container but in the same formatting context (e.g. floated columns). For example:

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: '';
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

Note that using a more modern approach, such as the flexbox or grid layout, is recommended over using `float` to build layouts.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
