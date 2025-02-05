# 旋转加载器

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

**渲染一个旋转加载器组件。**

要渲染一个旋转加载器组件，请执行以下步骤：

1. 渲染一个 SVG 元素，其尺寸由 `size` 属性决定。
2. 使用 CSS 为 SVG 添加动画，创建一个旋转动画。具体来说，将 `.loader` 类添加到 SVG 并将 `animation` 属性设置为 `rotate 2s linear infinite`。此外，使用 `transform` 属性定义 `rotate` 关键帧，使 SVG 旋转 360 度。
3. 向 SVG 添加一个 `circle` 元素，它代表旋转的圆圈。为了给圆圈添加动画，添加 `.loader circle` 选择器并将 `animation` 属性设置为 `dash 1.5s ease-in-out infinite`。此外，使用 `stroke-dasharray` 和 `stroke-dashoffset` 属性定义 `dash` 关键帧，创建一个围绕圆圈移动的虚线描边图案。
4. 最后，创建一个 `Loader` 组件，它将传入 `size` 属性的 SVG 渲染为宽度和高度属性。

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

要使用尺寸为 24 的 `Loader` 组件，请调用 `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`。

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
