# 自定义滚动条

虚拟机中已经提供了 `index.html` 和 `style.css`。

要为具有可滚动溢出的元素自定义滚动条样式，你可以使用 `::-webkit-scrollbar` 来设置滚动条元素的样式，使用 `::-webkit-scrollbar-track` 来设置滚动条轨道（滚动条的背景）的样式，以及使用 `::-webkit-scrollbar-thumb` 来设置滚动条滑块（可拖动的元素）的样式。不过请注意，此技术仅适用于基于 WebKit 的浏览器，并且滚动条样式不在任何标准轨道上。以下是在 HTML 和 CSS 中使用这些选择器的示例：

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
