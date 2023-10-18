# Fit Image in Container

`index.html` and `style.css` have already been provided in the VM.

To fit an image inside its container while preserving its aspect ratio, you can use `object-fit: contain`. To fill the container with the image while preserving its aspect ratio, use `object-fit: cover`. If you want to position the image at the center of the container, you can use `object-position: center`.

Here's an example of how you can use these properties:

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

And the corresponding CSS:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
