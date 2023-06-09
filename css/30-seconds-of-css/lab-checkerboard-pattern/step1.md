# Checkerboard Background Pattern

`index.html` and `style.css` have already been provided in the VM.

To create a checkerboard background pattern, follow these steps:

1. Set the `background-color` property to white.
2. Use `background-image` with two `linear-gradient()` values, each with a different angle to create the checkerboard pattern. For example, set one angle to `45deg` and the other to `-45deg`.
3. Specify the pattern's size using `background-size`. For instance, `60px 60px` will create a 60-by-60 pixel pattern.
4. Use `background-repeat` to set the repetition of the pattern. For example, `repeat` will make the pattern repeat in both directions.
5. Note that the `height` and `width` properties of the element are fixed to 240px for demonstration purposes.

Here's an example HTML element with the `.checkerboard` class:

```html
<div class="checkerboard"></div>
```

And here's the corresponding CSS:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
