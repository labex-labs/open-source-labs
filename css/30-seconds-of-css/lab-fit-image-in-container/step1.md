# How to Fit an Image in its Container

To fit and position an image within its container while preserving its aspect ratio, follow these steps:

1. Add the image to the HTML file using the `img` tag and specify the `src` attribute to the image URL.
2. To apply the desired fit and position settings, add the appropriate classes to the image tag.
    - Use the class `image-contain` to fit the entire image within the container while preserving its aspect ratio.
    - Use the class `image-cover` to fill the container with the image while preserving its aspect ratio.
3. In the CSS file, apply the following properties to the `image` class:
    - `background` to set the background color of the container.
    - `border` to add a border around the container.
    - `width` and `height` to set the dimensions of the container.

Example code:

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```