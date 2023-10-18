# Popout Menu

`index.html` and `style.css` have already been provided in the VM.

To reveal an interactive popout menu on hover/focus, follow these steps:

1. Use `left: 100%` in the CSS to position the popout menu to the right of the parent element.
2. Use `visibility: hidden` instead of `display: none` to hide the popout menu initially, to allow for transitions to be applied.
3. Apply `:hover`, `:focus`, and `:focus-within` pseudo-class selectors to the parent element to display the popout menu when it's hovered/focused.
4. Use the following HTML and CSS code:

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover > .popout-menu,
.reference:focus > .popout-menu,
.reference:focus-within > .popout-menu {
  visibility: visible;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
