# 风格化的引号

虚拟机中已经提供了 `index.html` 和 `style.css`。

要自定义内联引号，请修改 `<q>` 元素内的 `quotes` 属性。

例如：

```html
<p><q>Do or do not, there is no try.</q> – Yoda</p>
```

可以使用 CSS 用花括号引号来设置样式：

```css
q {
  quotes: "“" "”";
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
