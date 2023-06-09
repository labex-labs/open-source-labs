# Masonry Layout

`index.html` and `style.css` have already been provided in the VM.

To create a masonry-style layout, use the `.masonry-container` as the main container, and add `.masonry-columns` as an inner container to which `.masonry-brick` elements will be placed. The layout consists of "bricks" that fall into each other, forming a perfect fit. The `width` for a vertical layout, and `height` for a horizontal layout, can be fixed.

To ensure the layout flows properly, apply `display: block` to `.masonry-brick` elements. Use the `:first-child` pseudo-element selector to apply a different `margin` for the first element to account for its positioning.

For greater flexibility and responsiveness, use CSS variables and media queries. The `.masonry-container` has CSS variables for column count and gap. The number of columns is controlled by media queries that specify different column counts and widths for different screen sizes.

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="An image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="One more image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="And another one"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Last one"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
