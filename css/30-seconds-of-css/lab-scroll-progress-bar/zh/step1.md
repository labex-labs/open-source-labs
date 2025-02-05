# 滚动进度条

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个显示网页滚动百分比的进度条，请按照以下步骤操作：

1. 在 HTML 代码中添加一个 `id` 为 "scroll-progress" 的 `div` 元素。
2. 在 CSS 代码中，将该元素的 `position` 设置为 `fixed`，`top` 设置为 `0`，`width` 设置为 `0%`，`height` 设置为 `4px`，`background` 颜色设置为 `#7983ff`。
3. 将 `z-index` 值设置为一个较大的数字，以确保进度条位于页面顶部且在任何内容之上。
4. 在 JavaScript 代码中，使用 `document.getElementById()` 方法选择 `scroll-progress` 元素。
5. 使用公式 `document.documentElement.scrollHeight - document.documentElement.clientHeight` 计算网页的高度。
6. 向 `window` 对象添加一个事件监听器，监听 `scroll` 事件。
7. 在事件监听器函数中，使用公式 `(scrollTop / height) * 100` 计算文档的滚动百分比。
8. 使用 `style` 属性将 `scroll-progress` 元素的 `width` 设置为滚动百分比。

以下是代码：

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
