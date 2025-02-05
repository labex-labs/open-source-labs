# 工具提示

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

以下是更清晰、简洁和连贯的内容版本：

---

此代码创建了一个工具提示组件。要使用它，请执行以下操作：

1. 使用 `useState()` 钩子创建 `show` 变量并将其设置为 `false`。
2. 渲染一个容器元素，该元素包含工具提示元素和传递给组件的 `children`。
3. 通过切换由 `show` 变量控制的工具提示的 `className` 来处理 `onMouseEnter` 和 `onMouseLeave` 事件。

以下是工具提示组件的代码：

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

要使用工具提示组件，请使用以下代码调用 `ReactDOM.createRoot()`：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>
);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页以预览网页。

---
