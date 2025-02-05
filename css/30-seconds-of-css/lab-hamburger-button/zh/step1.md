# 汉堡按钮

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个在悬停时转换为关闭按钮的汉堡菜单，请按照以下步骤操作：

1. 使用一个 `.hamburger-menu` 容器 `div`，其中包含顶部、底部和中间的条。
2. 将容器设置为 `display: flex` 并使用 `flex-flow: column wrap`。
3. 使用 `justify-content: space-between` 在条之间添加间距。
4. 使用 `transform: rotate()` 将顶部和底部的条旋转 45 度，并使用 `opacity: 0` 在悬停时使中间的条渐变消失。
5. 使用 `transform-origin: left` 使条围绕左点旋转。

以下是相应的 HTML 代码：

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

以下是 CSS 代码：

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu.bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover.top {
  transform: rotate(45deg);
}

.hamburger-menu:hover.middle {
  opacity: 0;
}

.hamburger-menu:hover.bottom {
  transform: rotate(-45deg);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
