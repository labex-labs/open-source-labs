# 兄弟元素渐变

虚拟机中已经提供了 `index.html` 和 `style.css`。

要使鼠标悬停元素的兄弟元素渐隐：

1. 使用 `transition` 属性为 `opacity` 的变化添加动画效果。

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. 使用 `:hover` 和 `:not` 伪类选择器，将鼠标未悬停其上的所有元素的 `opacity` 设置为 `0.5`。

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

以下是一个 HTML 代码示例：

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
