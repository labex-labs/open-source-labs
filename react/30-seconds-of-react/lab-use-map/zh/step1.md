# React useMap 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

- `useMap()` 钩子使用 React 钩子创建一个有状态的 `Map` 对象以及一组用于操作它的函数。
- `useState()` 钩子使用 `initialValue` 初始化 `Map` 状态。
- `useMemo()` 钩子创建一组不可变的操作，这些操作每次使用状态设置器来操作 `map` 状态变量，从而创建一个新的 `Map`。
- `useMap()` 钩子返回一个数组，其中包含 `map` 状态变量和创建的 `actions`。
- `MyApp` 组件使用 `useMap()` 钩子初始化有状态的 `Map` 对象，并提供按钮用于向 `Map` 中添加、重置和移除项目。
- `JSON.stringify()` 函数将 `Map` 对象格式化为可读的 JSON 字符串。

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>添加</button>
      <button onClick={handleReset}>重置</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        移除 apples
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
