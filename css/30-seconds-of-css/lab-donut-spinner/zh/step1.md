# 甜甜圈加载指示器

虚拟机中已经提供了 `index.html` 和 `style.css`。

为了表示内容正在加载，创建一个甜甜圈加载指示器，整个元素使用半透明的 `border`。排除一侧作为甜甜圈的加载指示器。然后，定义并使用适当的动画，使用 `transform: rotate()` 来旋转元素。以下是 HTML 和 CSS 的示例代码：

HTML：

```html
<div class="donut"></div>
```

CSS：

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
