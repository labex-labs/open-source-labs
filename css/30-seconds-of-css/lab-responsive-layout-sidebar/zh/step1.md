# 带有侧边栏的响应式布局

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个包含内容区域和侧边栏的响应式布局，请在父容器上使用 `display: grid`，对第二列（侧边栏）使用 `minmax()`，使其宽度在 `150px` 到 `20%` 之间，对第一列（主要内容）使用 `1fr` 来占据剩余空间。以下是一个HTML和CSS代码示例：

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

请点击右下角的“Go Live”以在端口8080上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
