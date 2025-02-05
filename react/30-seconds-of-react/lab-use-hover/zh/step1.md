# React useHover 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这段代码创建了一个自定义钩子，用于处理悬停在包裹组件上的情况。

要使用这个钩子：

- 使用 `useState()` 创建一个变量来保存悬停状态。
- 使用 `useCallback()` 来记忆两个用于更新状态的处理函数。
- 使用 `useCallback()` 创建一个回调引用，并为 `'mouseover'` 和 `'mouseout'` 事件创建或更新监听器。
- 使用 `useRef()` 来跟踪最后传递给 `callbackRef` 的节点，以便能够移除其监听器。

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

这是该钩子的一个使用示例：

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "悬停中" : "未悬停"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
