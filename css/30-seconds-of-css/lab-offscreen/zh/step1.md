# 屏幕外

虚拟机中已提供了 `index.html` 和 `style.css`。

此技术可在 DOM 中完全隐藏一个元素，同时仍使其可访问。要实现这一点，你可以按以下步骤操作：

- 移除所有边框和内边距，并隐藏元素的溢出内容。
- 使用 `clip` 确保元素的任何部分都不显示。
- 将元素的 `高度` 和 `宽度` 设置为 `1px`，并使用 `margin: -1px` 使其为负。
- 使用 `position: absolute` 防止元素在 DOM 中占用空间。
- 请注意，就可访问性和布局友好性而言，此技术是 `display: none`（屏幕阅读器无法读取）和 `visibility: hidden`（在 DOM 中占用实际空间）的更好替代方案。

以下是在 HTML 和 CSS 中使用此技术的示例：

```html
<a class="button" href="https://google.com">
  Learn More <span class="offscreen">about pants</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
