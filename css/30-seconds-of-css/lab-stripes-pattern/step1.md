# Stripes Background Pattern

`index.html` and `style.css` have already been provided in the VM.

This code creates a vertical stripe pattern on a white background.

To create the pattern:

- Set the `background-color` property to white.
- Use `background-image` with a `linear-gradient()` value to create a vertical stripe.
- Set the `background-size` property to specify the size of each stripe.
- Set `background-repeat` to `repeat` to allow the pattern to fill the element.

Note that the fixed `width` and `height` of the element are for demonstration purposes only.

Here's an example code snippet:

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
