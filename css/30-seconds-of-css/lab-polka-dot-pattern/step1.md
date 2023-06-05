# Polka Dot Background Pattern

This code block creates a polka dot background pattern. Follow these instructions to implement it in your project:

1. Open `index.html` and `style.css`.
2. In `index.html`, create a `div` element with the class `polka-dot`.
3. In `style.css`, add the following rules to the `.polka-dot` selector:
   - Set `width` and `height` to `240px`.
   - Set `background-color` to black (`#000`).
   - Use `background-image` with two `radial-gradient()` values to create two dots.
   - Use `background-size` to specify the pattern's size. 
   - Use `background-position` to appropriately place the two gradients.
   - Set `background-repeat` to `repeat`.
4. Note that the fixed `height` and `width` of the element is for demonstration purposes only.

```html
<div class="polka-dot"></div>
```

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image: radial-gradient(#fff 10%, transparent 11%), radial-gradient(#fff
        10%, transparent 11%);
  background-size: 60px 60px;
  background-position: 0 0, 30px 30px;
  background-repeat: repeat;
}
```