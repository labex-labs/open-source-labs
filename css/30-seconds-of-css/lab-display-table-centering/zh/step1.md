# 使用表格显示实现元素居中

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在父元素内将子元素垂直和水平居中，请执行以下步骤：

1. 添加一个具有固定 `高度` 和 `宽度` 的容器元素。

```html
<div class="container"></div>
```

2. 在容器元素内添加子元素，并为其赋予 `.center` 类。

```html
  <div class="center"><span>Centered content</span></div>
</div>
```

3. 在 CSS 中，对容器元素应用以下样式：

- 将 `高度` 和 `宽度` 设置为所需的固定值。
- 添加边框（可选）。

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. 在 CSS 中，对 子元素应用以下样式：

- 使用 `display: table` 使 `.center` 元素表现得像一个 `<table>` 元素。
- 将 `高度` 和 `宽度` 设置为 `100%`，使元素填充其父元素内的可用空间。
- 在子元素上使用 `display: table-cell` 使其表现得像一个 `<td>` 元素。
- 在子元素上使用 `text-align: center` 和 `vertical-align: middle` 使其在水平和垂直方向上居中。

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

请点击右下角的 “Go Live” 在端口 8080 上运行网络服务。然后，你可以刷新 “Web 8080” 标签页来预览网页。
