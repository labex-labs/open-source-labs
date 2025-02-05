# 带顶部三角形的边框

虚拟机中已提供了 `index.html` 和 `style.css`。

要创建一个顶部带有三角形的内容容器，请执行以下步骤：

1. 使用 `::before` 和 `::after` 伪元素创建两个三角形。
2. 将三角形的 `border-color` 和 `background-color` 设置为与容器匹配。
3. 将 `::before` 三角形的 `border-width` 设置得比 `::after` 三角形宽 `1px`，以作为边框。
4. 将 `::after` 三角形定位在 `::before` 三角形右侧 `1px` 处，以便显示左边框。

以下是容器的示例 HTML 代码：

```html
<div class="container">Border with top triangle</div>
```

以下是相应的 CSS 代码：

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
