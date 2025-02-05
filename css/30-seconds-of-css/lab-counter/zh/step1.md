# 计数器

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个考虑嵌套列表元素的自定义列表计数器，请执行以下步骤：

1. 使用 `counter-reset` 初始化一个变量计数器（默认值为 `0`），其名称为属性的值（例如 `counter`）。
2. 对每个可数元素（例如每个 `<li>`）使用 `counter-increment` 递增变量计数器。
3. 使用 `counters()` 为每个可数元素（例如每个 `<li>`）的 `::before` 伪元素的 `content` 部分显示每个变量计数器的值。传递给它的第二个值（`'.'`）用作嵌套计数器的分隔符。

以下是一个示例 HTML 代码：

```html
<ul>
  <li>列表项</li>
  <li>列表项</li>
  <li>
    列表项
    <ul>
      <li>列表项</li>
      <li>列表项</li>
      <li>列表项</li>
    </ul>
  </li>
</ul>
```

以下是应用自定义列表计数器的 CSS 代码：

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
