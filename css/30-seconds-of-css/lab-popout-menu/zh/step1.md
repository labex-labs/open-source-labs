# 弹出式菜单

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在悬停/聚焦时显示交互式弹出式菜单，请执行以下步骤：

1. 在 CSS 中使用 `left: 100%` 将弹出式菜单定位在父元素的右侧。
2. 最初使用 `visibility: hidden` 而不是 `display: none` 来隐藏弹出式菜单，以便应用过渡效果。
3. 将 `:hover`、`:focus` 和 `:focus-within` 伪类选择器应用于父元素，以便在悬停/聚焦时显示弹出式菜单。
4. 使用以下 HTML 和 CSS 代码：

HTML：

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS：

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover >.popout-menu,
.reference:focus >.popout-menu,
.reference:focus-within >.popout-menu {
  visibility: visible;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
