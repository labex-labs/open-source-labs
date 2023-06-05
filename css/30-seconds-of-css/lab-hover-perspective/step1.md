# Applying a Perspective Transform with a Hover Animation

To apply a perspective transform with a hover animation to an element, follow these steps:

1. In `index.html` and `style.css`, create a container element with two child elements having the class `image-card`.
2. Use the CSS `transform` property with the `perspective()` and `rotateY()` functions to create a perspective for the element. Set the `rotateY()` value to positive for the left element and negative for the right element.
3. Use a CSS `transition` to update the `transform` attribute's value on hover.
4. Change the `rotateY()` value to a smaller angle on hover to create a mirror perspective effect.

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

```css
.card-container {
  display: flex;
  justify-content: center;
}

.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left,
.perspective-right {
  transform: perspective(1500px);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}

.perspective-left {
  transform-origin: right center;
  transform: rotateY(15deg) perspective(1500px);
}

.perspective-right {
  transform-origin: left center;
  transform: rotateY(-15deg) perspective(1500px);
}
```
