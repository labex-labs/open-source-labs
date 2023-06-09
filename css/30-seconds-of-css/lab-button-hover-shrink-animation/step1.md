# Button Shrink Animation

`index.html` and `style.css` have already been provided in the VM.

To create a shrink animation on hover for an element, you can use an appropriate `transition` property to animate changes and the `:hover` pseudo-class to trigger the animation. For example, if you want to shrink a button with class `button-shrink` when a user hovers over it, you can add the following CSS:

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

This will apply a transition effect to all properties of the button when there is a change, and when the user hovers over it, the button will shrink to 80% of its original size. The HTML code for the button is as follows:

```html
<button class="button-shrink">Submit</button>
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
