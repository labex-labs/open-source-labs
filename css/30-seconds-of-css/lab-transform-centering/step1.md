# Transform Centering

`index.html` and `style.css` have already been provided in the VM.

To vertically and horizontally center a child element within its parent using CSS transforms, follow these steps:

1. Set the `position` property of the parent element to `relative` and that of the child element to `absolute` to position it relative to its parent.
2. Use `left: 50%` and `top: 50%` to offset the child element 50% from the left and top edge of the parent element.
3. Use `transform: translate(-50%, -50%)` to negate its position, so that it is both vertically and horizontally centered.
4. Note that the fixed `height` and `width` of the parent element are for demonstration purposes only.

Here is an example HTML code:

```html
<div class="parent">
  <div class="child">Centered content</div>
</div>
```

And here is the corresponding CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
