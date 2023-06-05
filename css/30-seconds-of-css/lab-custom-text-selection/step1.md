# Custom Text Selection

To change the styling of text selection, write the code in `index.html` and `style.css` and use the `::selection` pseudo-selector. For instance:

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```