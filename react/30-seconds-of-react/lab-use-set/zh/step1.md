# React useSet 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此函数创建一个带有状态的 `Set` 对象以及一组可操作该状态的函数。

要使用此函数：

- 调用 `useState()` 和 `Set` 构造函数，从 `initialValue` 创建一个新的 `Set`。
- 使用 `useMemo()` 创建一组不可变的函数，这些函数可操作 `set` 状态变量。每次都使用状态设置器创建一个新的 `Set`。
- 返回 `set` 状态变量和创建的 `actions`。

以下是此函数的一个示例实现：

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

以下是此函数的一个示例用法：

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>添加</button>
      <button onClick={() => clear()}>重置</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        移除苹果
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
