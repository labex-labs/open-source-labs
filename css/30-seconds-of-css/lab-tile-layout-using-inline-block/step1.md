# 3-Tile Layout

`index.html` and `style.css` have already been provided in the VM.

To create a 3-tile layout, use `display: inline-block` instead of `float`, `flex`, or `grid`. Use `width` in combination with `calc` to divide the width of the container evenly into 3 columns. To avoid whitespace, set `font-size` to `0` for `.tiles` and to `20px` for `<h2>` elements to display the text. Note that using `font-size: 0` to fight whitespace between blocks might cause side effects if you use relative units (e.g. `em`).

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150">
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150">
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150">
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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
