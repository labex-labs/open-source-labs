# Hover Shadow Box Animation

`index.html` and `style.css` have already been provided in the VM.

To create a shadow box around the text when it is hovered, follow these steps:

1. Set `transform: perspective(1px)` to give the element a 3D space by affecting the distance between the Z plane and the user, and `translateZ(0)` to reposition the `p` element along the z-axis in 3D space.
2. Use `box-shadow` to make the box transparent.
3. Enable transitions for both `box-shadow` and `transform` by using the `transition-property` property.
4. Apply a new `box-shadow` and `transform: scale(1.2)` to change the scale of the text by using the `:hover`, `:active`, and `:focus` pseudo-class selectors.
5. Add the class `hover-shadow-box-animation` to the `p` element.

Here's the HTML code:

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

And here's the CSS code:

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
