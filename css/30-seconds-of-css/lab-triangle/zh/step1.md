# 三角形

虚拟机中已提供 `index.html` 和 `style.css`。

要使用纯 CSS 创建三角形，请执行以下步骤：

1. 使用三个具有相同 `border-width`（`20px`）的边框来创建三角形形状。
2. 将三角形指向的对边的 `border-color` 设置为所需颜色。相邻边框的 `border-color` 应为 `transparent`（透明）。
3. 要调整三角形的大小，请更改 `border-width` 值。

以下是一个示例代码片段：

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
