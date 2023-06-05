# Responsive Image Mosaic

This code creates a responsive image mosaic using `index.html` and `style.css`.

To create the mosaic, a responsive grid layout is used (`display: grid`), and the items that span two rows or two columns are created using `grid-row: span 2 / auto` and `grid-column: span 2 / auto`, respectively. To avoid applying the previous styles on small screen sizes, they are wrapped into a media query.

```html
<div class="image-mosaic">
  <div class="card card-tall card-wide" style="background-image: url('https://picsum.photos/id/564/1200/800')"></div>
  <div class="card card-tall" style="background-image: url('https://picsum.photos/id/566/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/575/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/626/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/667/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/678/800/530')"></div>
  <div class="card card-wide" style="background-image: url('https://picsum.photos/id/695/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/683/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/693/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/715/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/610/800/530')"></div>
  <div class="card" style="background-image: url('https://picsum.photos/id/599/800/530')"></div>
</div>
```

```css
.image-mosaic {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  grid-auto-rows: 240px;
}

.card {
  background: #353535;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 4px;
  box-shadow: rgba(3, 8, 20, 0.1) 0px 0.15rem 0.5rem, rgba(2, 8, 20, 0.1) 0px 0.075rem
      0.175rem;
  color: #fff;
  display: flex;
  flex-direction: column;
  font-size: 3rem;
  height: 100%;
  justify-content: center;
  margin: 0;
  overflow: hidden;
  padding: 0;
  transition: all 500ms;
  width: 100%;
}

@media screen and (min-width: 600px) {
  .card-tall {
    grid-row: span 2 / auto;
  }

  .card-wide {
    grid-column: span 2 / auto;
  }
}
```