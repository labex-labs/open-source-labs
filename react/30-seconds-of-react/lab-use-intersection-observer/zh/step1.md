# React 的 useIntersectionObserver 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要观察给定元素的可见性变化，请执行以下步骤：

1. 使用 `useState()` 钩子存储给定元素的交叉值。
2. 使用给定的 `options` 创建一个 `IntersectionObserver`，并使用适当的回调函数来更新 `isIntersecting` 状态变量。
3. 使用 `useEffect()` 钩子在挂载组件时调用 `IntersectionObserver.observe()`，并在卸载时使用 `IntersectionObserver.unobserve()` 进行清理。

以下是一个示例实现：

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

你可以像这样使用 `useIntersectionObserver` 钩子：

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>向下滚动</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "元素在屏幕上。" : "继续滚动！"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
