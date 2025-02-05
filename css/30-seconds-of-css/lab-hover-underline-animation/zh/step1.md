# 悬停下划线动画

虚拟机中已提供了 `index.html` 和 `style.css`。

要在用户将鼠标悬停在文本上时创建动画下划线效果，请执行以下步骤：

1. 使用 `display: inline-block` 使下划线仅跨越文本内容的宽度。
2. 将 `::after` 伪元素与 `width: 100%` 和 `position: absolute` 一起使用，将其放置在内容下方。
3. 使用 `transform: scaleX(0)` 最初隐藏伪元素。
4. 使用 `:hover` 伪类选择器应用 `transform: scaleX(1)` 并在悬停时显示伪元素。
5. 使用 `transform-origin: left` 和适当的 `transition` 为 `transform` 添加动画效果。
6. 移除 `transform-origin` 属性以使变换从元素中心开始。

以下是将该效果应用于文本元素的示例 HTML 代码：

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

以及相应的 CSS 代码：

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
