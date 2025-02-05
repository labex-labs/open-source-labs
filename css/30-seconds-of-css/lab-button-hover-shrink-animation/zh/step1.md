# 按钮收缩动画

虚拟机中已经提供了 `index.html` 和 `style.css`。

要为某个元素创建悬停时的收缩动画，你可以使用适当的 `transition` 属性来为变化添加动画效果，并使用 `:hover` 伪类来触发动画。例如，如果你想在用户悬停在一个类名为 `button-shrink` 的按钮上时使其收缩，你可以添加如下 CSS：

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

这将在按钮发生变化时为其所有属性应用过渡效果，并且当用户悬停在按钮上时，按钮会缩小到其原始大小的 80%。该按钮的 HTML 代码如下：

```html
<button class="button-shrink">Submit</button>
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
