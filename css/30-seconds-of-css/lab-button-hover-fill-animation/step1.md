# Button Fill Animation

`index.html` and `style.css` have already been provided in the VM.

To create a fill animation on hover, you can set the `color` and `background` properties and apply an appropriate `transition` to animate the changes. To trigger the animation on hover, use the `:hover` pseudo-class to change the `background` and `color` properties of the element. Here's an example code snippet:

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
