# 3-Tile Layout

To create a 3-tile layout without using `float`, `flex`, or `grid`, use `display: inline-block`. In `index.html` and `style.css`, follow these steps:

1. Set the width of `.tiles` to `600px`.
2. Set `font-size` to `0` for `.tiles` to avoid whitespace and to `20px` for `<h2>` elements to display the text.
3. Inside `.tiles`, create three equal-width columns using `width` and `calc` to divide the width of the container.
4. In each column, create a `.tile` div that contains an image and an `<h2>` element with the text you want to display.

**Note:** Be aware that if you use relative units (e.g. `em`), using `font-size: 0` to fight whitespace between blocks might cause side effects.

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```