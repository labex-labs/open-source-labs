# Hiding Scroll Bars

To hide scrollbars on an element while allowing it to be scrollable, use the following code in your `index.html` and `style.css` files:

```html
<div class="no-scrollbars">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
div {
  width: 200px;
  height: 100px;
}

.no-scrollbars {
  overflow: auto;
  scrollbar-width: none;
}

.no-scrollbars::-webkit-scrollbar {
  display: none;
}
```

Here's what each line of CSS does:

- `overflow: auto` allows the element to be scrollable.
- `scrollbar-width: none` hides scrollbars on Firefox.
- `display: none` on the `::-webkit-scrollbar` pseudo-element hides scrollbars on WebKit browsers like Chrome, Edge, and Safari.