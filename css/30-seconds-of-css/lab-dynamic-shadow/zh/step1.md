# 动态阴影

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建基于元素颜色的阴影，请执行以下步骤：

1. 使用 `::after` 伪元素，将 `position` 设置为 `absolute`，并将 `width` 和 `height` 设置为 `100%`，以填充父元素中的可用空间。

2. 使用 `background: inherit` 继承父元素的 `background`。

3. 使用 `top` 稍微偏移伪元素。然后，使用 `filter: blur()` 创建阴影，并设置 `opacity` 使其半透明。

4. 通过设置 `z-index: -1` 将伪元素定位在其父元素后面。在父元素上设置 `z-index: 1`。

以下是一个 HTML 和 CSS 代码示例：

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
