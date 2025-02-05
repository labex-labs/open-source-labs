# 宽高比

虚拟机中已经提供了 `index.html` 和 `style.css`。

这段代码使用 CSS 自定义属性和 `calc()` 函数创建了一个具有特定宽高比的响应式容器。按照以下步骤来实现：

1. 使用 CSS 自定义属性 `--aspect-ratio` 定义所需的宽高比。
2. 将容器元素的 `position` 属性设置为 `relative`，`height` 属性设置为 `0`。
3. 使用 `calc()` 函数和 `--aspect-ratio` 自定义属性计算容器元素的高度，并将其设置为 `padding-bottom` 属性。
4. 将容器元素的直接子元素设置为 `position: absolute`、`top: 0`、`left: 0`、`width: 100%` 和 `height: 100%`。
5. 通过将子元素的 `object-fit` 属性设置为 `cover` 来保持其宽高比。

使用以下 HTML 和 CSS 代码创建容器：

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
