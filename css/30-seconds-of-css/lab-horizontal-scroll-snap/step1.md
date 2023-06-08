# Horizontal Scroll Snap

This code creates a horizontally scrollable container that snaps on elements when scrolling. To implement this, follow these steps:

1. In your `index.html` and `style.css` files, write the code below.
2. Use `display: grid` and `grid-auto-flow: column` to create a horizontal layout.
3. Use `scroll-snap-type: x mandatory` and `overscroll-behavior-x: contain` to create a snap effect on horizontal scroll.
4. Change `scroll-snap-align` to either `start`, `stop` or `center` to change the snap alignment.

```html
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640" /></a>
</div>
```

```css
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  margin: 0 auto;
  max-width: 480px;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  padding: 1rem;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  border-radius: 1rem;
  max-width: none;
  object-fit: contain;
  width: 180px;
}
```
