# 脉冲加载器

虚拟机中已经提供了 `index.html` 和 `style.css`。

要使用 `animation-delay` 属性创建一个脉冲效果加载动画，请按照以下步骤操作：

1. 使用 `@keyframes` 为两个 `<div>` 元素定义一个动画。将两个元素的起始点（`0%`）设置为没有 `width` 或 `height`，并定位在中心位置。对于结束点（`100%`），让两个元素的 `width` 和 `height` 都增加，但将它们的 `position` 重置为 `0`。
2. 在动画时使用 `opacity` 从 `1` 过渡到 `0`，以便 `<div>` 元素在扩展时具有消失效果。
3. 为父容器 `.ripple-loader` 设置预定义的 `width` 和 `height`。使用 `position: relative` 来定位其子元素。
4. 在第二个 `<div>` 元素上使用 `animation-delay`，以便每个元素在不同的时间开始动画。

以下是实现此效果的 HTML 和 CSS 代码：

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
