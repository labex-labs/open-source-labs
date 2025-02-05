# React 的 useMergeState 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要创建一个有状态的值以及一个通过合并提供的新状态来更新它的函数，请使用 `useState()` 钩子创建一个状态变量并将其初始化为 `initialState`。创建一个函数，该函数将通过把提供的新状态与现有状态合并来更新状态变量。如果新状态是一个函数，则将前一个状态作为参数调用它并使用结果。如果未提供参数，则状态变量将初始化为一个空对象 (`{}`)。以下代码演示了如何使用 `useMergeState` 自定义钩子来实现这一点：

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

以下是 `useMergeState` 钩子在名为 `MyApp` 的组件中的一个使用示例：

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
