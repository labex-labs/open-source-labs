# React useMediaQuery 钩子

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

此函数检查当前环境是否匹配给定的媒体查询，并返回相应的值。

- 首先，检查 `Window` 和 `Window.matchMedia()` 是否存在。如果不存在（例如在 SSR 环境或不受支持的浏览器中），则返回 `whenFalse`。
- 使用 `Window.matchMedia()` 来匹配给定的 `query`。将其 `matches` 属性转换为布尔值，并使用 `useState()` 钩子将其存储在状态变量 `match` 中。
- 使用 `useEffect()` 钩子添加一个更改监听器，并在钩子销毁后清理监听器。
- 最后，根据 `match` 的值返回 `whenTrue` 或 `whenFalse`。

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "小于 400 像素宽",
    "大于 400 像素宽"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
