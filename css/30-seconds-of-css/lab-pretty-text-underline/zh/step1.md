# 美观的文本下划线

虚拟机中已经提供了 `index.html` 和 `style.css`。

为避免下行字母裁剪下划线，使用具有四个值的 `text-shadow` 创建一个粗阴影，覆盖下行字母与下划线相交的线条。确保 `text-shadow` 颜色与 `background` 颜色匹配，并根据较大字体调整 `px` 值。使用带有 `linear-gradient()` 和 `currentColor` 的 `background-image` 创建实际的下划线。设置 `background-position`、`background-repeat` 和 `background-size` 将渐变放置在正确的位置。使用 `::selection` 伪类选择器确保文本阴影不会干扰文本选择。请注意，此效果原生实现为 `text-decoration-skip-ink: auto`，但对下划线的控制较少。

以下是一个示例代码片段：

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
