# 截断文本

虚拟机中已经提供了 `index.html` 和 `style.css`。

要截断超过一行的文本并在末尾添加省略号，请使用以下 CSS 属性：

- `overflow: hidden` 防止文本超出其尺寸范围
- `white-space: nowrap` 防止文本在高度上超过一行
- `text-overflow: ellipsis` 如果文本超出其尺寸范围，则添加省略号
- 为元素指定固定的 `width`，以便知道何时显示省略号

请注意，此方法仅适用于单行元素。例如：

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
