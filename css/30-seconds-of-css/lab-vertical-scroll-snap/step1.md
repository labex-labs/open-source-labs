# Vertical Scroll Snap

`index.html` and `style.css` have already been provided in the VM.

Revised content:

This code creates a scrollable container that snaps to elements while scrolling. To achieve this effect, the following steps are taken:

1. `display: grid` and `grid-auto-flow: row` are used to create a vertical layout.
2. `scroll-snap-type: y mandatory` and `overscroll-behavior-y: contain` are used to create the snap effect on vertical scroll.
3. `scroll-snap-align` with either `start`, `stop` or `center` can be used to change the snap alignment.

Here's the HTML and CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
