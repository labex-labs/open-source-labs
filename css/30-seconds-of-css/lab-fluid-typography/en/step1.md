# Fluid Typography

`index.html` and `style.css` have already been provided in the VM.

To create text that adjusts in size based on the width of the viewport, you can use CSS. One way to do this is by using the `clamp()` function to set the minimum and maximum font sizes. Another way is to use a formula to calculate a responsive value for the font size. Here is an example HTML element with a class of `fluid-type`:

```html
<p class="fluid-type">Hello World!</p>
```

Here is the corresponding CSS code that sets the font size to adjust between `1rem` and `3rem` based on the viewport width:

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
