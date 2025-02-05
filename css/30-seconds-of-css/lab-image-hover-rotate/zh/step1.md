# 悬停时图像旋转

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在悬停时为图像创建旋转效果，当鼠标悬停在父元素（应为 `<figure>` 元素）上时，使用 `scale()`、`rotate()` 和 `transition` 属性。为确保图像变换不会超出父元素范围，在父元素的 CSS 中添加 `overflow: hidden`。以下是一个 HTML 和 CSS 代码示例：

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
