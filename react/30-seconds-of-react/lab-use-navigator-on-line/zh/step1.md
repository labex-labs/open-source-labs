# React useNavigatorOnLine 钩子

> VM 中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要检查客户端是在线还是离线，你可以创建一个利用 `Navigator.onLine` Web API 的 `getOnLineStatus` 函数。然后，要在 React 组件中实现此功能，你可以使用 `useNavigatorOnLine` 自定义钩子。此钩子使用 `useState()` 钩子创建一个名为 `status` 的状态变量，并将其设置为 `getOnLineStatus()` 返回的值。`useEffect()` 钩子用于为在线/离线状态变化添加事件监听器，相应地更新 `status` 状态变量，并在组件卸载时清理这些监听器。最后，`useNavigatorOnLine()` 返回的 `isOnline` 变量可用于渲染一条消息，指示客户端是在线还是离线。

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>你是 {isOnline ? "在线" : "离线"}。</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
