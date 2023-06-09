# Isometric Card

`index.html` and `style.css` have already been provided in the VM.

To create an isometric card, use `transform` with `rotateX()` and `rotateY()` along with a `box-shadow`. You can also add a `transition` to animate the card and create a lift effect when the user hovers over it.

Here's an example code snippet:

```html
<div class="isometric-card"></div>
```

```css
.isometric-card {
  margin: 0 auto;
  transform: rotateX(51deg) rotateZ(43deg);
  transform-style: preserve-3d;
  background-color: #fcfcfc;
  will-change: transform;
  width: 240px;
  height: 320px;
  border-radius: 2rem;
  box-shadow: 1px 1px 0 1px #f9f9fb, -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    28px 28px 28px 0 rgba(34, 33, 81, 0.25);
  transition: transform 0.4s ease-in-out, box-shadow 0.3s ease-in-out;
}

.isometric-card:hover {
  transform: translate3d(0px, -16px, 0px) rotateX(51deg) rotateZ(43deg);
  box-shadow: 1px 1px 0 1px #f9f9fb, -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    54px 54px 28px -10px rgba(34, 33, 81, 0.15);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
