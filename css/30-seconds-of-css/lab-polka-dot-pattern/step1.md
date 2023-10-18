# Polka Dot Background Pattern

`index.html` and `style.css` have already been provided in the VM.

To create a polka dot background pattern, you can follow these steps:

1. Set the `background-color` property to black.
2. Use the `background-image` property with two `radial-gradient()` values to create two dots.
3. Specify the pattern's size using the `background-size` property. Use `background-position` to appropriately place the two gradients.
4. Set `background-repeat` to `repeat`.
5. Note that the fixed `height` and `width` of the element is for demonstration purposes only.

Here's an example HTML code for a div element with class `polka-dot`:

```html
<div class="polka-dot"></div>
```

And here's the corresponding CSS code:

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image: radial-gradient(#fff 10%, transparent 11%), radial-gradient(#fff
        10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
