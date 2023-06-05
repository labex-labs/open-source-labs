# Triangle

To create a triangular shape with pure CSS, follow these steps:

1. Open the `index.html` and `style.css` files.
2. Use the following code to create a triangle shape:
```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```
3. To customize the triangle:
    - Use three borders to form a triangle.
    - Set all the borders' `border-width` to `20px`.
    - Set the `border-color` of the opposite side of the triangle's point (top if the triangle points downwards) to the desired color.
    - Set the `border-color` of the adjacent borders (left and right) to `transparent`.
    - Modify the `border-width` values to change the triangle's proportions.

Example usage:
```html
<div class="triangle"></div>
```