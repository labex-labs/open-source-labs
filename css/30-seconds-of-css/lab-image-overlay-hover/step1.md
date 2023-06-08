# Image Overlay on Hover

To create an image overlay effect on hover, follow these steps:

1. In `index.html`, use the `<figure>` and `<figcaption>` elements to wrap the image and text respectively. Add the `hover-img` class to the `<figure>` element.

```html
<figure class="hover-img">
  <img src="https://picsum.photos/id/200/440/320.jpg" />
  <figcaption>
    <h3>Lorem <br />Ipsum</h3>
  </figcaption>
</figure>
```

2. In `style.css`, apply the following styles to the `.hover-img` class:

```css
.hover-img {
  background-color: #000;
  color: #fff;
  display: inline-block;
  margin: 8px;
  max-width: 320px;
  min-width: 240px;
  overflow: hidden;
  position: relative;
  text-align: center;
  width: 100%;
}
```

3. Apply the following styles to all child elements of `.hover-img`:

```css
.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}
```

4. Use the `::before` and `::after` pseudo-elements to create the top and bottom bars of the overlay respectively. Apply the following styles:

```css
.hover-img::before,
.hover-img::after {
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  content: "";
  transition: all 0.3s ease;
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
}
```

5. Apply the following styles to the `<img>` element to ensure it is aligned with the text:

```css
.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}
```

6. Apply the following styles to the `<figcaption>` element to center the text:

```css
.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}
```

7. Finally, use the `:hover` pseudo-selector to update the opacity and transform of all the elements and display the overlay:

```css
.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover > img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
```
