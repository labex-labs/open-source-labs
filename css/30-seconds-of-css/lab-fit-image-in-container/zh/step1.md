# 在容器中适配图像

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在保持宽高比的同时将图像适配到其容器内，可以使用 `object-fit: contain`。要在保持宽高比的同时用图像填充容器，可使用 `object-fit: cover`。如果你想将图像定位在容器的中心，可以使用 `object-position: center`。

以下是如何使用这些属性的示例：

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

以及相应的 CSS：

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

请点击右下角的“Go Live”在 8080 端口运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
