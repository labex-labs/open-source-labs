# 圆形

虚拟机中已经提供了 `index.html` 和 `style.css`。

要使用纯 CSS 创建圆形，可使用 `border-radius: 50%` 属性来使元素的边框弯曲。确保将 `width` 和 `height` 设置为相同的值，以确保得到一个完美的圆形。如果使用不同的值，将创建一个椭圆。以下是一个示例代码片段：

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
