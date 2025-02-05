# 等距卡片

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个等距卡片，可使用 `transform` 搭配 `rotateX()` 和 `rotateZ()` 以及 `box-shadow`。你还可以添加一个 `transition` 来为卡片添加动画效果，并在用户悬停在卡片上时创建一种抬起的效果。

以下是一个示例代码片段：

```html
<div class="isometric-card"></div>
```

```css
.isometric-card {
  margin: 0 auto;
  transform: rotateX(51deg) rotateZ(43deg);
  transform-style: preserve-3d;
  background-color: #fcfcfc;
  will-change: transform;
  width: 240px;
  height: 320px;
  border-radius: 2rem;
  box-shadow:
    1px 1px 0 1px #f9f9fb,
    -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    28px 28px 28px 0 rgba(34, 33, 81, 0.25);
  transition:
    transform 0.4s ease-in-out,
    box-shadow 0.3s ease-in-out;
}

.isometric-card:hover {
  transform: translate3d(0px, -16px, 0px) rotateX(51deg) rotateZ(43deg);
  box-shadow:
    1px 1px 0 1px #f9f9fb,
    -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    54px 54px 28px -10px rgba(34, 33, 81, 0.15);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
