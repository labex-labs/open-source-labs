# Horizontal Scroll Snap

`index.html` and `style.css` have already been provided in the VM.

To create a horizontally scrollable container that snaps on elements when scrolling, follow these steps:

1. Use `display: grid` and `grid-auto-flow: column` to create a horizontal layout.
2. Use `scroll-snap-type: x mandatory` and `overscroll-behavior-x: contain` to create a snap effect on horizontal scroll.
3. Change `scroll-snap-align` to either `start`, `stop` or `center` to adjust the snap alignment.

Here's an example HTML and CSS code you can use:

HTML
```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS
```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
