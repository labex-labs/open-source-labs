# Sibling Fade

`index.html` and `style.css` have already been provided in the VM.

To fade out the siblings of a hovered item:

1. Animate changes to `opacity` using the `transition` property.

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. Change the `opacity` of all elements except for the one the mouse is over to `0.5` using the `:hover` and `:not` pseudo-class selectors.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

Here's an example HTML code:

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
