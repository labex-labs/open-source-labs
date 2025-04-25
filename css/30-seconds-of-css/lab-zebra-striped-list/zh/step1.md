# 斑马条纹列表

虚拟机中已提供了 `index.html` 和 `style.css`。

要创建具有交替背景颜色的列表，请使用 `:nth-child(odd)` 或 `:nth-child(even)` 伪类选择器，根据元素在同级元素中的位置为其应用不同的 `background-color`。这可以应用于各种 HTML 元素，如 `<div>`、`<tr>`、`<p>`、`<ol>` 等。

以下是如何使用 `<li>` 元素创建条纹列表的示例：

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
