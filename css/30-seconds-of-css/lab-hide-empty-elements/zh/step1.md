# 隐藏空元素

虚拟机中已提供了 `index.html` 和 `style.css`。

要隐藏没有内容的元素，请使用 `:empty` 伪类。例如，如果你有以下 HTML 代码：

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

你可以使用以下 CSS 代码来隐藏没有内容的按钮元素：

```css
p:empty {
  display: none;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
