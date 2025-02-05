# 带文本覆盖的图像

虚拟机中已经提供了 `index.html` 和 `style.css`。

要显示带有文本覆盖的图像，请使用 `<figure>` 和 `<figcaption>` 元素。在 CSS 中使用 `linear-gradient` 属性在图像上创建覆盖效果。以下是一个示例代码片段：

```html
<figure class="text-overlay-image">
  <img src="https://picsum.photos/id/971/400/400.jpg" />
  <figcaption>
    <h3>Business <br />Pricing</h3>
  </figcaption>
</figure>
```

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}

.text-overlay-image figcaption {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(0deg, #00000088 30%, #ffffff44 100%);
  color: #fff;
  padding: 16px;
  font: 700 28px/1.2 sans-serif;
}

.text-overlay-image figcaption h3 {
  margin: 0;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
