# 按钮边框动画

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在悬停时创建边框动画，你可以使用 `::before` 和 `::after` 伪元素来生成两个宽度为 `24px` 的框，并将它们定位在按钮框的上方和下方。然后，应用 `:hover` 伪类，在悬停时将这些元素的 `宽度` 增加到 `100%`，并使用 `transition` 为过渡添加动画效果。

以下是一个示例代码片段：

```html
<button class="animated-border-button">提交</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
