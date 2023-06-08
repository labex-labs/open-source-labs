# Flexbox Centering

To horizontally and vertically center a child element within a parent element using flexbox, you can write the code in `index.html` and `style.css` as follows:

- Use `display: flex` to create a flexbox layout.
- Use `justify-content: center` to center the child horizontally.
- Use `align-items: center` to center the child vertically.

```html
<div class="flexbox-centering">
  <div>Centered content.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```
