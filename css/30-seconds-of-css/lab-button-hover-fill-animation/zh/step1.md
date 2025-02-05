# 按钮填充动画

虚拟机中已提供 `index.html` 和 `style.css`。

要创建悬停时的填充动画，你可以设置 `颜色` 和 `背景` 属性，并应用适当的 `过渡` 来为更改设置动画。要在悬停时触发动画，使用 `:hover` 伪类来更改元素的 `背景` 和 `颜色` 属性。以下是一个示例代码片段：

```html
<button class="animated-fill-button">提交</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
