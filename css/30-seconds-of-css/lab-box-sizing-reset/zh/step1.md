# 盒模型大小重置

虚拟机中已经提供了 `index.html` 和 `style.css`。

为确保元素的 `宽度` 和 `高度` 不受 `边框` 或 `内边距` 的影响，请使用CSS属性 `box-sizing: border-box`。这会将 `内边距` 和 `边框` 包含在元素 `宽度` 和 `高度` 的计算中。如果你想从父元素继承 `box-sizing` 属性，请使用 `box-sizing: inherit`。

以下是对两个 `div` 元素使用 `box-sizing` 属性的示例：

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

在此示例中，第一个 `div` 元素的 `box-sizing` 为 `border-box`，第二个 `div` 元素的 `box-sizing` 为 `content-box`。

请点击右下角的 “Go Live” 在端口8080上运行网络服务。然后，你可以刷新 “Web 8080” 标签页来预览网页。
