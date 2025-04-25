# 加载失败图像的备用方案

虚拟机中已提供 `index.html` 和 `style.css`。

当图像加载失败时，向用户显示错误消息。为此，将样式应用于 `img` 元素，就好像它是一个文本容器一样，将其显示设置为块级元素，并将其宽度设置为 100%。使用 `::before` 和 `::after` 伪元素分别显示错误消息和图像 URL。只有在图像加载失败时，这些元素才会显示。

以下是一个示例代码片段：

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
