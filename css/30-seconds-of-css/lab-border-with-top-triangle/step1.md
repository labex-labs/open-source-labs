# Creating a Content Container with a Triangle at the Top

To create a content container with a triangle at the top, follow these steps:
1. Open the `index.html` and `style.css` files.
2. In the HTML file, create a `div` element with the class of `container` and add the text "Border with top triangle" inside it.
3. In the CSS file, set the `position` of the `container` class to `relative`, `background` to `#ffffff`, `padding` to `15px`, `border` to `1px solid #dddddd`, and `margin-top` to `20px`.
4. To create the triangles, use the `::before` and `::after` pseudo-elements.
5. Set the `content` property to an empty string for both pseudo-elements.
6. Set the `position` of both pseudo-elements to `absolute`, `bottom` to `100%`, `left` to `19px`.
7. For the `::before` triangle, set `border` to `11px solid transparent`, and `border-bottom-color` to `#dddddd`.
8. For the `::after` triangle, set `left` to `20px`, `border` to `10px solid transparent`, and `border-bottom-color` to `#ffffff`.
9. The `border-width` of the `::before` triangle should be `1px` wider than the `::after` triangle to act as the border.
10. The `::after` triangle should be `1px` to the right of the `::before` triangle to allow for its left border to be shown.

Here's the updated code:

```html
<div class="container">Border with top triangle</div>
```

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
}

.container::before {
  border: 11px solid transparent;
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```