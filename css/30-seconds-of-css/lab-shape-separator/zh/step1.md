# 形状分隔符

虚拟机中已经提供了 `index.html` 和 `style.css`。

要使用 SVG 形状在两个不同的块之间创建一个分隔元素，请按照以下步骤操作：

1. 使用 `::after` 伪元素。
2. 通过 `background-image` 属性，使用数据 URI 添加 SVG 形状（一个 24x12 的三角形）。默认情况下，背景图像会重复并覆盖伪元素的整个区域。
3. 使用父元素的 `background` 属性为分隔符设置所需的颜色。

使用以下 HTML 代码：

```html
<div class="shape-separator"></div>
```

并应用以下 CSS 规则：

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
