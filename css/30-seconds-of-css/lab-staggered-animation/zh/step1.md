# 交错动画

虚拟机中已经提供了 `index.html` 和 `style.css`。

这段代码为列表元素创建了交错动画。实现步骤如下：

1. 通过设置 `opacity: 0` 和 `transform: translateX(100%)`，使列表元素透明并一直移动到右侧。
2. 为列表元素指定相同的 `transition` 属性，但不包括 `transition-delay`。
3. 使用内联样式为每个列表元素指定 `--i` 的值。这将用于 `transition-delay` 以创建交错效果。
4. 对复选框使用 `:checked` 伪类选择器来设置列表元素的样式。为了使它们出现并滑入视图，将 `opacity` 设置为 `1`，将 `transform` 设置为 `translateX(0)`。

以下是实现此效果的 HTML 和 CSS 代码：

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
