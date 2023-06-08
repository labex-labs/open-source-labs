# Image With Text Overlay

`index.html` and `style.css` have already been provided in the VM.

To display an image with a text overlay, use the `<figure>` and `<figcaption>` elements. Use the `linear-gradient` property in CSS to create the overlay effect over the image. Here is an example code snippet:

```html
<figure class="text-overlay-image">
  <img src="https://picsum.photos/id/971/400/400.jpg" />
  <figcaption>
    <h3>Business <br/>Pricing</h3>
  </figcaption>
</figure>
```

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}

.text-overlay-image figcaption {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(0deg, #00000088 30%, #ffffff44 100%);
  color: #fff;
  padding: 16px;
  font: 700 28px/1.2 sans-serif;
}

.text-overlay-image figcaption h3 {
  margin: 0;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
