# React 的 useRequestAnimationFrame 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要在每次重绘之前运行一个动画函数，可以使用 `useRef()` 钩子来创建 `requestRef` 和 `previousTimeRef` 变量。然后，定义一个 `animate()` 函数，该函数更新这些变量，运行 `callback`，并持续调用 `Window.requestAnimationFrame()`。最后，使用 `useEffect()` 钩子并传入一个空数组，用 `Window.requestAnimationFrame()` 初始化 `requestRef` 的值，并在组件卸载时使用返回值和 `Window.cancelAnimationFrame()` 进行清理。

以下是 `useRequestAnimationFrame()` 的一个示例实现：

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

要在组件中使用这个自定义钩子，只需向它传递一个回调函数。例如，要创建一个以 100 FPS 更新的简单计数器：

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
