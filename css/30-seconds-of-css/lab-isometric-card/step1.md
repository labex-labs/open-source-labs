# Isometric Card

This code block creates an isometric card. The code is written in `index.html` and `style.css`.

To create the card, use `transform` with `rotateX()` and `rotateY()`, as well as a `box-shadow`. The card is contained within a `div` with a class of `isometric-card`. The card has a width of `240px`, a height of `320px`, and a `border-radius` of `2rem`. The `background-color` is `#fcfcfc`.

To animate the card, add a `transition` that creates a lift effect when the user hovers over it. The `transition` should include `ease-in-out` and have a duration of `0.4s` for the `transform` property, and `0.3s` for the `box-shadow` property.

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
