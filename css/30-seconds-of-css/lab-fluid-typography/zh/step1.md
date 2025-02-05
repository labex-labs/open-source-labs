# 流体排版

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建根据视口宽度调整大小的文本，你可以使用 CSS。一种方法是使用 `clamp()` 函数来设置最小和最大字体大小。另一种方法是使用公式来计算字体大小的响应式值。以下是一个具有 `fluid-type` 类的 HTML 元素示例：

```html
<p class="fluid-type">Hello World!</p>
```

以下是相应的 CSS 代码，它根据视口宽度将字体大小设置为在 `1rem` 和 `3rem` 之间调整：

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
