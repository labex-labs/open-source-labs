# React useIsomporphicEffect 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

为了确保在服务器上正确使用 `useEffect()`，在客户端正确使用 `useLayoutEffect()`，你可以使用 `typeof` 来检查 `Window` 对象是否已定义。如果已定义，返回 `useLayoutEffect()`，否则返回 `useEffect()`。以下是实现此功能的示例：

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

然后，在你的代码中，你可以像这个例子一样使用 `useIsomorphicEffect()`：

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

当组件挂载时，这将在控制台中输出 'Hello'，并且在服务器和客户端上都能正常工作。

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
