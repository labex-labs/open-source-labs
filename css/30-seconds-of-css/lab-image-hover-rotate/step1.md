# Creating a Hover Effect to Rotate an Image

To create a rotate effect for an image on hover, follow these steps:

1. In the `index.html` file, add the following code:

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

2. In the `style.css` file, add the following CSS:

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

This will animate the image on hover using the `scale()`, `rotate()`, and `transition` properties. The `overflow: hidden` property on the parent element (`<figure>`) will hide the excess from the image transformation.
