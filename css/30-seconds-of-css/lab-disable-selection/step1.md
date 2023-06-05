# Disable Selection

To make the content of an element unselectable, add the CSS property `user-select: none`. However, note that this method is not secure for preventing users from copying content.

Example usage:
```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```