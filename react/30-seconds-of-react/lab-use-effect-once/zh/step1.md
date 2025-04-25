# React useEffectOnce 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

以下代码实现了一个函数 `useEffectOnce(callback, when)`，当 `when` 条件变为真时，该函数只会运行一次 `callback`。

要实现此函数：

- 使用 `useRef()` 钩子创建一个变量 `hasRunOnce`，以跟踪副作用的执行状态。
- 使用仅在 `when` 条件发生变化时运行的 `useEffect()` 钩子。
- 在 `useEffect()` 钩子内部，检查 `when` 是否为 `true` 且副作用之前未执行过。如果两者都为 `true`，则运行 `callback` 并将 `hasRunOnce` 设置为 `true`。

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

以下是 `useEffectOnce()` 的一个示例用法：

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

在这个示例中，`useEffectOnce()` 用于在按钮首次被点击时将“mounted”打印到控制台。`useEffectOnce()` 钩子接收两个参数：要运行的 `callback` 和要检查的 `when` 条件。`when` 条件被设置为 `clicked` 状态，因此只有当 `clicked` 首次变为 `true` 时，`callback` 才会运行。

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
