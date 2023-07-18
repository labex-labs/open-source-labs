# Button Grow Animation

`index.html` and `style.css` have already been provided in the VM.

To create a grow animation on hover, you can use an appropriate `transition` to animate changes to the element. Use the `:hover` pseudo-class to change the `transform` property to `scale(1.1)`. This will grow the element when the user hovers over it.

Here is an example code snippet you can use:

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
