# How to Display an Image with Text Overlay

To display an image with a text overlay, follow these steps:

1. In your HTML file (`index.html`), create a `figure` element with a class of `text-overlay-image`.
2. Inside the `figure` element, add an `img` element with the source URL of your desired image.
3. Also inside the `figure` element, add a `figcaption` element.
4. Inside the `figcaption` element, add your desired text. Use HTML tags as needed to format the text.
5. In your CSS file (`style.css`), add the following styles to the `.text-overlay-image` class:

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}
```

6. Next, add the following styles to the `.text-overlay-image figcaption` selector:

```css
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
  font-family: sans-serif;
  font-weight: 700;
  line-height: 1.2;
  font-size: 28px;
}
```

7. Finally, add the following styles to the `.text-overlay-image figcaption h3` selector:

```css
.text-overlay-image figcaption h3 {
  margin: 0;
}
```

This will create a text overlay effect over the image using a linear gradient. The `h3` element within the `figcaption` will be styled with white text on top of the gradient.
