# Vertical Scroll Snap

To create a scrollable container that snaps on elements when scrolling vertically, you can write the code in `index.html` and `style.css`. Here are the steps to follow:

- Create a vertical layout using `display: grid` and `grid-auto-flow: row`.
- To create a snap effect on vertical scroll, use `scroll-snap-type: y mandatory` and `overscroll-behavior-y: contain`.
- You can use `scroll-snap-align` with either `start`, `stop` or `center` to change the snap alignment.

Use the following HTML code:

```html
<div class="vertical-snap">
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

And the following CSS code:

```css
.vertical-snap {
  margin: 0 auto;
  display: grid;
  grid-auto-flow: row;
  gap: 1rem;
  width: calc(180px + 1rem);
  padding: 1rem;
  height: 480px;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-snap-type: y mandatory;
}

.vertical-snap > a {
  scroll-snap-align: center;
}

.vertical-snap img {
  width: 180px;
  object-fit: contain;
  border-radius: 1rem;
}
```
