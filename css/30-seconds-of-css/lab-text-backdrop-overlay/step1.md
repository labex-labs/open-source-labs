# Image Text Overlay

To display a text on top of an image using an overlay, write the code in `index.html` and `style.css`. Use `backdrop-filter` to apply a `blur(14px)` and `brightness(80%)` effect, which makes the text readable regardless of the background image and color.

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

The CSS code should be as follows:

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```
