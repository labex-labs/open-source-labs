# 图像文本叠加

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在带有叠加效果的图像上显示文本，请使用 `backdrop-filter` 属性来应用 `blur(14px)` 和 `brightness(80%)` 效果。这可确保无论背景图像和颜色如何，文本都清晰可读。以下是一个 HTML 代码示例：

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

以及相应的 CSS 代码：

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
