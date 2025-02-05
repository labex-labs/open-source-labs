# 截断多行文本

虚拟机中已经提供了 `index.html` 和 `style.css`。

要截断超过一行的文本，请执行以下步骤：

1. 使用 `overflow: hidden` 防止文本超出其尺寸范围。
2. 设置固定宽度为 `400px`，以确保元素至少有一个固定尺寸。
3. 根据公式 `font-size * line-height * numberOfLines`（在本例中为 `26 * 1.4 * 3 = 109.2`），将高度设置为 `109.2px`。
4. 在 HTML 中的 `p` 元素上添加类 `truncate-text-multiline`。
5. 在 CSS 中为 `.truncate-text-multiline` 类设置 `font-size: 26px` 和 `line-height: 1.4`。
6. 设置 `color: #333` 和 `background: #f5f6f9` 来设置文本样式。
7. 要创建从 `transparent` 到 `background-color` 的渐变，请将以下 CSS 规则添加到 `.truncate-text-multiline::after` 伪元素：

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

这将创建一个高度为 `36.4px` 的渐变容器，该高度是根据公式 `font-size * line-height`（在本例中为 `26 * 1.4 = 36.4`）为渐变容器计算得出的。`::after` 伪元素位于 `.truncate-text-multiline` 元素的右下角。

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
