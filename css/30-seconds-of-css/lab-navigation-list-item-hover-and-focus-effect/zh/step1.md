# 导航列表项悬停和聚焦效果

虚拟机中已经提供了 `index.html` 和 `style.css`。

要为导航项创建自定义悬停和聚焦效果，请按以下方式使用 CSS 变换：

1. 在列表项锚点处使用 `::before` 伪元素来创建悬停效果。使用 `transform: scale(0)` 将其隐藏。
2. 使用 `:hover` 和 `:focus` 伪类选择器将伪元素过渡到 `transform: scale(1)` 并显示其彩色背景。
3. 通过使用 `z-index` 防止伪元素覆盖锚点元素。

你可以在导航菜单中使用以下 HTML 代码：

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

并应用以下 CSS 规则：

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
