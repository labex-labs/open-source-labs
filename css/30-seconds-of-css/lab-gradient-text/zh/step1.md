# 渐变文本

虚拟机中已经提供了 `index.html` 和 `style.css`。

要给文本设置渐变颜色，可以使用 CSS 属性。首先，将 `background` 属性与 `linear-gradient()` 值一起使用，为文本元素设置渐变背景。然后，使用 `webkit-text-fill-color: transparent` 用透明颜色填充文本。最后，使用 `webkit-background-clip: text` 将背景裁剪为文本形状，并用渐变背景作为颜色填充文本。以下是一个示例代码片段：

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

请点击右下角的“Go Live”，在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
