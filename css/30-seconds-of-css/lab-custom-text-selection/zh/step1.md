# 自定义文本选择

虚拟机中已提供了 `index.html` 和 `style.css`。

若要修改所选文本的样式，请使用 `::selection` 伪选择器。以下是一个用于选择并设置段落元素内文本样式的代码片段示例：

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

请点击右下角的“Go Live”，以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
