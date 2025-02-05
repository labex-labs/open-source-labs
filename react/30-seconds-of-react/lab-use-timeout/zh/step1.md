# React useTimeout 钩子

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要以声明式方式实现 `setTimeout()`，创建一个自定义钩子，它接受一个 `callback` 和一个 `delay`。使用 `useRef()` 钩子为回调函数创建一个 `ref`，并使用 `useEffect()` 钩子记住最新的回调。然后，使用 `useEffect()` 钩子设置超时并进行清理。

以下是一个演示此方法的示例代码片段：

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<OneSecondTimer />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
