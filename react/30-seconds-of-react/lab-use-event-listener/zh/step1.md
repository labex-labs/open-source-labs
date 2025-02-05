# React useEventListener 钩子

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

此函数会为给定元素上指定的事件类型添加一个事件监听器。要使用此函数，请执行以下步骤：

1. 使用 `useRef()` 钩子创建一个引用，用于保存 `handler`。
2. 使用 `useEffect()` 钩子，每当 `handler` 发生变化时更新 `savedHandler` 引用的值。
3. 使用 `useEffect()` 钩子向给定元素添加一个事件监听器，并在卸载时进行清理。
4. 省略最后一个参数 `el`，默认使用 `Window`。

以下是代码：

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

以下是 `useEventListener()` 函数的一个示例用法：

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      鼠标坐标：{coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
