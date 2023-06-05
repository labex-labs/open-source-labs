# Sibling Fade

To create a fade-out effect for the siblings of a hovered item, follow these steps:

1. Open `index.html` and `style.css`.
2. In the HTML file, create a `div` with the class `sibling-fade`. Inside it, add several `span` elements with names or labels.
3. In the CSS file, target all `span` elements and add padding and a transition property that animates changes to `opacity`.
4. Use the `:hover` and `:not` pseudo-class selectors to change the `opacity` of all elements except for the one the mouse is over to `0.5`.

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}

.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```
