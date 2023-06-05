# Fluid Typography

To create text that scales according to the viewport width, use the code in `index.html` and `style.css`. The following steps can be followed:

- Use the `clamp()` CSS function to set the range of `font-size` between `1rem` and `3rem`.
- Use the formula `8vw - 2rem` to calculate a responsive value for `font-size` where `1rem` is set at `600px` and `3rem` at `1000px`.
- Add the following code in `index.html` where you want the text to appear:

```html
<p class="fluid-type">Hello World!</p>
```

- Add the following CSS code in `style.css` to apply the fluid typography effect to the text:

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```