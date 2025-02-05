# React useUnload 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

可以通过以下步骤处理 `beforeunload` 窗口事件：

1. 使用 `useRef()` 钩子为回调函数 `fn` 创建一个引用。
2. 使用 `useEffect()` 钩子和 `EventTarget.addEventListener()` 来处理 `'beforeunload'` 事件，该事件在用户即将关闭窗口时触发。
3. 使用 `EventTarget.removeEventListener()` 在组件卸载后执行清理操作。

以下是代码：

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("你确定要离开吗？");
    if (exit) window.close();
  });

  return <div>尝试关闭窗口。</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
