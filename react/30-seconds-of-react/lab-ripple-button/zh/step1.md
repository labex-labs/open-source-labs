# 带有涟漪效果的按钮

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这段代码渲染了一个按钮组件，点击时会产生涟漪效果。其工作原理如下：

- `useState()` 钩子用于创建两个状态变量：`coords` 和 `isRippling`。`coords` 变量存储指针的坐标，而 `isRippling` 存储按钮的动画状态。
- `useEffect()` 钩子用于每当 `coords` 状态变量发生变化时，改变 `isRippling` 的值。这会启动涟漪效果的动画。
- 在上一个钩子中使用 `setTimeout()` 在动画播放完毕后清除动画。
- 另一个 `useEffect()` 钩子用于每当 `isRippling` 状态变量为 `false` 时重置 `coords`。
- `onClick` 事件通过更新 `coords` 状态变量并调用传递的回调函数来处理。

以下是 `RippleButton` 组件的代码：

```jsx
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={(e) => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling && (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

你可以像这样使用这个组件：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <RippleButton onClick={(e) => console.log(e)}>Click me</RippleButton>
);
```

以下是 `RippleButton` 组件的 CSS：

```css
.ripple-button {
  border-radius: 4px;
  border: none;
  margin: 8px;
  padding: 14px 24px;
  background: #1976d2;
  color: #fff;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.ripple-button > .ripple {
  width: 20px;
  height: 20px;
  position: absolute;
  background: #63a4ff;
  display: block;
  content: "";
  border-radius: 9999px;
  opacity: 1;
  animation: 0.9s ease 1 forwards ripple-effect;
}

@keyframes ripple-effect {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(10);
    opacity: 0.375;
  }
  100% {
    transform: scale(35);
    opacity: 0;
  }
}

.ripple-button > .content {
  position: relative;
  z-index: 2;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
