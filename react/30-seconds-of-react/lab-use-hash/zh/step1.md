# React useHash 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码用于跟踪和更新浏览器的位置哈希值。使用方法如下：

1. 使用 `useState()` 钩子来惰性获取 `Location` 对象的 `hash` 属性。
2. 使用 `useCallback()` 钩子创建一个事件处理函数，当触发 `'hashchange'` 事件时更新 `hash` 状态。
3. 使用 `useEffect()` 钩子在挂载时添加 `'hashchange'` 事件监听器，并在卸载时清除它。
4. 使用 `useCallback()` 钩子创建一个函数，用给定的值更新 `Location` 对象的 `hash` 属性。
5. 在你的组件中，调用 `useHash()` 以获取当前的 `hash` 值和一个 `updateHash()` 函数来更改它。
6. 使用 `updateHash()` 函数更改 `hash` 值。
7. 在组件中渲染当前的 `hash` 值。
8. 创建一个输入字段，允许用户更改 `hash` 值。

以下是代码：

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>当前哈希值：{hash}</p>
      <p>编辑哈希值：</p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
