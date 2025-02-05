# React 的 useOnGlobalEvent 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这个函数会在全局对象上发生事件时执行一个回调函数。要实现这个函数：

1. 使用 `useRef()` 钩子创建一个变量 `listener`，它将保存监听器引用。
2. 使用 `useRef()` 钩子创建一个变量，用于保存 `type` 和 `options` 参数的前一个值。
3. 使用 `useEffect()` 钩子和 `EventTarget.addEventListener()` 在 `Window` 全局对象上监听给定的事件 `type`。
4. 使用 `EventTarget.removeEventListener()` 移除任何现有的监听器，并在组件卸载时进行清理。

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

以下是如何使用这个函数的示例：

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
