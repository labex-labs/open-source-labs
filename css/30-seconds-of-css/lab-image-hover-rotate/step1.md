# Image Rotate on Hover

`index.html` and `style.css` have already been provided in the VM.

To create a rotate effect for an image on hover, use the `scale()`, `rotate()`, and `transition` properties when hovering over the parent element, which should be a `<figure>` element. To ensure the image transformation doesn't overflow from the parent element, add `overflow: hidden` to the parent element's CSS. Here's an example HTML and CSS code:

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg"/>
</figure>
```

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
