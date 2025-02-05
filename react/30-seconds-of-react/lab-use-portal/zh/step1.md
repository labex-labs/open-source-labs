# React usePortal 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要创建一个在父组件外部渲染子组件的门户，请执行以下步骤：

1. 使用 `useState()` 钩子创建一个状态变量，该变量保存门户的 `render()` 和 `remove()` 函数。
2. 使用 `ReactDOM.createPortal()` 和 `ReactDOM.unmountComponentAtNode()` 创建一个门户和一个移除它的函数。使用 `useCallback()` 钩子将这些函数包装并记忆化为 `createPortal()`。
3. 使用 `useEffect()` 钩子在 `el` 的值发生变化时调用 `createPortal()` 并更新状态变量。
4. 最后，返回状态变量的 `render()` 函数。

以下是一个示例实现：

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

要使用此钩子，创建一个组件，将所需的 DOM 元素作为参数调用 `usePortal()`。然后，该组件可以使用返回的 `render()` 函数在门户中渲染内容：

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      你好，世界！
      <Portal>门户化标题</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
