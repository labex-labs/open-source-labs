# React useOnWindowResize Hook

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码会在每次窗口大小改变时执行一个回调函数。要实现它，你应遵循以下步骤：

1. 使用 `useRef()` Hook 创建一个名为 `listener` 的变量。这个变量将存储监听器的引用。

2. 使用 `useEffect()` Hook 和 `EventTarget.addEventListener()` 来监听 `Window` 全局对象的 `'resize'` 事件。当事件触发时，调用 `callback` 函数。

3. 在组件卸载时，通过 `EventTarget.removeEventListener()` 移除任何现有的监听器来进行清理。

以下是代码：

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Window size: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return <p>Resize the window and check the console.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
