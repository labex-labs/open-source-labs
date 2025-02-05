# React useToggler 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要创建一个可以在两种状态之间切换的布尔状态变量，请按照以下步骤操作：

1. 使用 `useState()` 钩子创建 `value` 状态变量及其设置函数。
2. 创建一个函数，用于切换 `value` 状态变量的值，并使用 `useCallback()` 钩子对其进行记忆化。
3. 返回 `value` 状态变量和记忆化的切换函数。

以下是一个示例实现：

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

然后，你可以在组件中使用这个钩子，如下所示：

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
