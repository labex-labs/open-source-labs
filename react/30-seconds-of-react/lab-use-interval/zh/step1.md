# React useInterval 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要以声明式方式实现 `setInterval()`，你可以创建一个自定义钩子，它接受一个 `回调函数` 和一个 `延迟时间`。第一步是使用 `useRef()` 钩子为回调函数创建一个 `ref`。然后，每当 `回调函数` 发生变化时，使用 `useEffect()` 钩子记住最新的 `回调函数`。最后，使用依赖于 `延迟时间` 的 `useEffect()` 钩子来设置时间间隔并进行清理。

以下是自定义钩子的示例代码片段：

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

然后，你可以在组件中使用这个自定义钩子。例如，要创建一个每秒更新一次的定时器：

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
