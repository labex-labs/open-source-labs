# 三栏布局

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建三栏布局，请使用 `display: inline-block`，而不是 `float`、`flex` 或 `grid`。结合使用 `width` 和 `calc` 将容器的宽度均匀地分成三列。为避免出现空白，将 `.tiles` 的 `font-size` 设置为 `0`，并将 `<h2>` 元素的 `font-size` 设置为 `20px` 以显示文本。请注意，如果使用相对单位（例如 `em`），使用 `font-size: 0` 来消除块之间的空白可能会产生副作用。

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

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
