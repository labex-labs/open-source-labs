# React useSSR 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要检查代码是在浏览器还是服务器上运行，创建一个自定义钩子，它使用 `typeof`、`Window`、`Window.document` 和 `Document.createElement()` 来确定 DOM 是否可用。使用 `useState()` 钩子定义 `inBrowser` 状态变量，并使用 `useEffect()` 钩子来更新它并在最后进行清理。使用 `useMemo()` 钩子来记忆自定义钩子的返回值。

以下是代码：

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return <p>{isBrowser ? "在浏览器上运行" : "在服务器上运行"}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
