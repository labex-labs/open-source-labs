# 网格居中

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在父元素内将子元素水平和垂直居中，请执行以下步骤：

1. 使用 `display: grid` 创建网格布局。
2. 使用 `justify-content: center` 将子元素水平居中。
3. 使用 `align-items: center` 将子元素垂直居中。

以下是一个示例 HTML 结构：

```html
<div class="parent">
  <div class="child">Centered content.</div>
</div>
```

以及相应的 CSS：

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
