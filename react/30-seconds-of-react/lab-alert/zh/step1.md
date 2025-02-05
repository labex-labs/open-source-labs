# 可关闭的警报

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

使用 `type` 属性渲染一个警报组件。

`Alert` 组件接受以下属性：

- `isDefaultShown`：一个布尔值，用于确定警报最初是否显示（默认值为 `false`）
- `timeout`：一个数字，指定警报淡出前的持续时间（以毫秒为单位）（默认值为 `250`）
- `type`：一个字符串，用于确定警报的类型（例如 "warning"、"error"、"info"）
- `message`：一个字符串，包含要在警报中显示的消息

该组件执行以下操作：

- 使用 `useState()` 钩子创建 `isShown` 和 `isLeaving` 状态变量，并将它们初始设置为 `false`。
- 定义一个 `timeoutId` 变量，用于保存定时器实例，以便在组件卸载时清除。
- 使用 `useEffect()` 钩子在组件挂载时将 `isShown` 的值更新为 `true`，并在组件卸载时使用 `timeoutId` 清除定时器。
- 定义一个 `closeAlert` 函数，通过显示淡出动画并通过 `setTimeout()` 将 `isShown` 设置为 `false`，将组件从 DOM 中移除。
- 如果 `isShown` 为 `true`，则渲染警报组件。该组件根据 `type` 属性具有适当的样式，如果 `isLeaving` 为 `true`，则会淡出。

以下是代码：

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert.close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert.close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签以预览网页。
