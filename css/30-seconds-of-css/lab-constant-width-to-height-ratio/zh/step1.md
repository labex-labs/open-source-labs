# 固定宽高比

虚拟机中已提供了 `index.html` 和 `style.css`。

此代码片段可确保宽度可变的元素保持成比例的高度值。要实现这一点，在 `::before` 伪元素上应用 `padding-top`，使元素的高度等于其宽度的某个百分比。高度与宽度的比例可根据需要进行更改。例如，`padding-top` 为 `100%` 将创建一个 1:1 比例的响应式正方形。要使用此代码，只需添加以下 HTML 代码：

```html
<div class="constant-width-to-height-ratio"></div>
```

然后，添加以下 CSS 代码：

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
