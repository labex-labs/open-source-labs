# React useDefault 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

以下是代码：

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

要创建一个带有默认回退值的有状态值，请在 React 中使用 `useState()` 钩子。检查初始值是否为 `null` 或 `undefined`。如果是，则返回 `defaultState`，否则返回实际的 `value` 状态和 `setValue` 函数。上面的代码展示了如何在一个名为 `useDefault` 的自定义钩子中实现此功能。

在提供的示例中，`useDefault` 用于创建一个默认值为 `{ name: 'Adam' }` 的 `user` 状态。初始状态设置为 `{ name: 'John' }`。在 `UserCard` 组件中，显示 `user` 以及一个用于更新其名称的输入字段。还提供了一个清除按钮，用于将状态重置为 `null`。最后，使用 `ReactDOM.createRoot()` 渲染组件。

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页以预览网页。
