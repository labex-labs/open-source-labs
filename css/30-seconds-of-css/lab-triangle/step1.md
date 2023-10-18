# Triangle

`index.html` and `style.css` have already been provided in the VM.

To create a triangular shape with pure CSS, follow these steps:

1. Use three borders with the same `border-width` (`20px`) to create the triangle shape.
2. Set the `border-color` of the opposite side of where the triangle points towards to the desired color. The adjacent borders should have a `border-color` of `transparent`.
3. To adjust the size of the triangle, alter the `border-width` values.

Here's an example code snippet:

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
