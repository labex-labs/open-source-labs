# 缩放动画

虚拟机中已提供了 `index.html` 和 `style.css`。

要创建缩放动画，请执行以下步骤：

1. 使用 `@keyframes` 定义一个三步动画。在 `0%` 和 `100%` 时，使用 `scale(1,1)` 将元素设置为其原始大小。在 `50%` 时，使用 `scale(1.5,1.5)` 将其放大到原始大小的 1.5 倍。

2. 使用 `width` 和 `height` 为元素设置特定大小。

3. 使用 `animation` 为元素设置适当的值以使其产生动画效果。

以下是一个 HTML 和 CSS 代码示例：

```html
<div class="zoom-in-out-box"></div>
```

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}

@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
