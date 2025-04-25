# 弹跳加载器

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个弹跳加载器动画：

1. 定义一个 `@keyframes` 动画，该动画使用 `opacity` 和 `transform` 属性，并在 `transform: translate3d()` 上进行单轴平移以获得更好的性能。
2. 创建一个类名为 `.bouncing-loader` 的父容器，使用 `display: flex` 和 `justify-content: center` 来使弹跳的圆圈居中。
3. 为弹跳圆圈的三个 `<div>` 元素赋予相同的 `width`、`height` 和 `border-radius: 50%`，使其成为圆形。
4. 将 `bouncing-loader` 动画应用于三个弹跳圆圈中的每一个。
5. 为每个圆圈使用不同的 `animation-delay` 并设置 `animation-direction: alternate` 以创建适当的效果。

以下是 HTML 代码：

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

以下是 CSS 代码：

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
