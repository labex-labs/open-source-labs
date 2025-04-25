# React useWindowSize 钩子

> VM 中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要跟踪浏览器窗口的尺寸，可以采取以下步骤：

1. 使用 `useState()` 钩子初始化一个状态变量 `windowSize`，用于保存窗口尺寸。初始时将两个值都设为 `undefined`，以避免服务器端渲染和客户端渲染之间的不匹配。

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. 创建一个函数 `handleResize()`，它使用 `Window.innerWidth` 和 `Window.innerHeight` 来更新状态变量。每当触发 `'resize'` 事件时，都会调用此函数。

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. 使用 `useEffect()` 钩子在挂载时为 `'resize'` 事件设置适当的监听器，并在卸载时清理它。

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

将上述内容整合起来，`useWindowSize()` 自定义钩子可以定义如下：

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

要使用 `useWindowSize()` 钩子，只需在组件中调用它，并从返回的对象中解构出 `width` 和 `height` 值。

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      窗口尺寸：({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
