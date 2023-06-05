# Button Grow Animation

To create a grow animation on hover, follow these steps:

1. Open `index.html` and `style.css`.
2. Add the following HTML code to create a button with a class of "button-grow":

```html
<button class="button-grow">Submit</button>
```

3. Add the following CSS code to style the button and create the grow animation on hover:

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

The `transition` property is used to animate changes to the element, and the `:hover` pseudo-class is used to change the `transform` property to `scale(1.1)`, which grows the element when the user hovers over it.
