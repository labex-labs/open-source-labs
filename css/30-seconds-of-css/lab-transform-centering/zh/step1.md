# 使用变换进行居中

虚拟机中已经提供了 `index.html` 和 `style.css`。

要使用 CSS 变换在父元素中垂直和水平居中子元素，请执行以下步骤：

1. 将父元素的 `position` 属性设置为 `relative`，子元素的 `position` 属性设置为 `absolute`，以便相对于其父元素进行定位。
2. 使用 `left: 50%` 和 `top: 50%` 将子元素从父元素的左边缘和上边缘偏移 50%。
3. 使用 `transform: translate(-50%, -50%)` 来抵消其位置，使其在垂直和水平方向上都居中。
4. 请注意，父元素固定的 `height` 和 `width` 仅用于演示目的。

以下是一个示例 HTML 代码：

```html
<div class="parent">
  <div class="child">Centered content</div>
</div>
```

以及相应的 CSS 代码：

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
