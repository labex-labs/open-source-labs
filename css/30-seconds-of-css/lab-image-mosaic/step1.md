# Responsive Image Mosaic

`index.html` and `style.css` have already been provided in the VM.

To create a responsive image mosaic, use `display: grid` to create a responsive grid layout with `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` and `grid-auto-rows: 240px`. To span items across two rows or two columns, use `grid-row: span 2 / auto` and `grid-column: span 2 / auto`. Finally, wrap these styles into a media query to avoid applying them to small screen sizes.

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
  display: flex;
  justify-content: center;
  align-items: center;
  background: #353535 url('https://picsum.photos/id/564/1200/800') center / cover no-repeat;
  font-size: 3rem;
  color: #fff;
  box-shadow: rgba(3, 8, 20, 0.1) 0px 0.15rem 0.5rem, rgba(2, 8, 20, 0.1) 0px 0.075rem 0.175rem;
  height: 100%;
  width: 100%;
  border-radius: 4px;
  transition: all 500ms;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.card-tall {
  grid-row: span 2 / auto;
}

.card-wide {
  grid-column: span 2 / auto;
}

@media screen and (max-width: 599px) {
  .card-tall,
  .card-wide {
    grid-row: span 1 / auto;
    grid-column: span 1 / auto;
  }
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
