# Transform Centering

To vertically and horizontally center a child element within its parent element using CSS transforms, follow these steps:

- Set the `position` of the parent to `relative` and the child to `absolute` to position it relative to its parent.
- Offset the child element 50% from the left and top edge of the containing block by using `left: 50%` and `top: 50%`.
- Use `transform: translate(-50%, -50%)` to negate its position, so that it is vertically and horizontally centered.
- Note that the fixed `height` and `width` of the parent element is only for demonstration purposes.

Here is an example of the HTML and CSS code:

```html
<div class="parent">
  <div class="child">Centered content</div>
</div>
```

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```
