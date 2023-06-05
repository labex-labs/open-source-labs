# Zig Zag Background Pattern

To create a zig zag background pattern, follow these steps:

1. Write the code in `index.html` and `style.css`.
2. Set the background color to white using `background-color`.
3. Use `background-image` to create four parts of the zig zag pattern with `linear-gradient()` values.
4. Specify the pattern's size using `background-size` and place the pattern parts in the correct locations using `background-position`.
5. Note that the fixed `height` and `width` of the element is for demonstration purposes only.

Here's the code you can use:

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%), linear-gradient(
      315deg,
      #000 25%,
      transparent 25%
    ), linear-gradient(45deg, #000 25%, transparent 25%);
  background-position: -30px 0, -30px 0, 0 0, 0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```