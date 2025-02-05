# 均匀分布子元素

虚拟机中已提供 `index.html` 和 `style.css`。

要在父元素内均匀分布子元素，请使用弹性盒布局，将父元素的 `display` 属性设置为 `flex`。要在水平方向上均匀分布子元素并使它们之间具有相等的间距，请使用 `justify-content: space-between`。要在子元素周围留出空间，请使用 `justify-content: space-around`。以下是一个示例：

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
