# Circle

`index.html` and `style.css` have already been provided in the VM.

To create a circular shape using pure CSS, use the `border-radius: 50%` property to curve the element's borders. Make sure to set both `width` and `height` to the same value to ensure a perfect circle. If different values are used, an ellipse will be created instead. Here's an example code snippet:

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
