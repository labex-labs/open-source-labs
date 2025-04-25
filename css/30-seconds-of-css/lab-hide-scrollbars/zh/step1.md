# 隐藏滚动条

虚拟机中已经提供了 `index.html` 和 `style.css`。

若要在隐藏滚动条的同时使元素可滚动，请执行以下步骤：

- 使用 `overflow: auto` 使元素能够滚动。
- 使用 `scrollbar-width: none` 在 Firefox 上隐藏滚动条。
- 在 `::-webkit-scrollbar` 伪元素上使用 `display: none` 来隐藏 WebKit 浏览器（如 Chrome、Edge 和 Safari）上的滚动条。

以下是一个示例实现：

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Hide scrollbars on WebKit browsers */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
