# Circle

To create a circular shape using pure CSS, add the following code to `index.html` and `style.css`.

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

- Use `border-radius: 50%` to curve the borders of the element and create a circle.
- Make sure to set the `width` and `height` of the element to the same value to achieve a perfect circle. Using different values will result in an ellipse.