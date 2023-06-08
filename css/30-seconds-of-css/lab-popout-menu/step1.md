# Popout Menu

To reveal an interactive popout menu on hover/focus, write the code in `index.html` and `style.css`.

Use the following CSS properties and selectors to achieve the desired result:

- `position: relative` for the parent element.
- `position: absolute`, `visibility: hidden`, and `left: 100%` for the popout menu.
- `:hover`, `:focus`, and `:focus-within` pseudo-class selectors to apply `visibility: visible` to the popout menu when the parent element is hovered/focused.

HTML code:

```html
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS code:

```css
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
  background: #9c27b0;
  color: white;
  padding: 16px;
}

.reference:hover > .popout-menu,
.reference:focus > .popout-menu,
.reference:focus-within > .popout-menu {
  visibility: visible;
}
```
