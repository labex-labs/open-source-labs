# 禁用选择

虚拟机中已提供了 `index.html` 和 `style.css`。

要使元素的内容不可选，可向选择器添加 CSS 属性 `user-select: none`。不过，这种方法并不能完全确保防止用户复制内容。

示例：

```html
<p>你可以选中我。</p>
<p class="unselectable">你无法选中我！</p>
```

```css
.unselectable {
  user-select: none;
}
```

请点击右下角的“Go Live”，在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
