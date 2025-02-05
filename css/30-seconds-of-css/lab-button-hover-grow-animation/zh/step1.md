# 按钮放大动画

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建悬停时的放大动画，你可以使用适当的 `transition` 来为元素的变化设置动画。使用 `:hover` 伪类将 `transform` 属性更改为 `scale(1.1)`。这样当用户悬停在元素上时，它就会放大。

以下是你可以使用的示例代码片段：

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
