# 为无文本的链接设置样式

虚拟机中已提供了 `index.html` 和 `style.css`。

要为无文本的链接显示链接 URL，你可以使用 `:empty` 伪类来选择此类链接，使用 `:not` 伪类来排除有文本的链接，并结合使用 `content` 属性和 `attr()` 函数在 `::before` 伪元素中显示链接 URL。以下是一个代码片段示例：

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
