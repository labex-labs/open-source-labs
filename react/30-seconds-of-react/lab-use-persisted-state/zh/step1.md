# React 的 usePersistedState 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这个钩子返回一个在 `localStorage` 中持久化的有状态值，以及一个可用于更新它的函数。要使用它，请遵循以下步骤：

1. 使用 `useState()` 钩子将 `value` 初始化为 `defaultValue`。
2. 使用 `useRef()` 钩子创建一个引用，该引用将在 `Window.localStorage` 中保存该值的 `name`。
3. 分别使用 3 个 `useEffect()` 钩子实例进行初始化、`value` 更改和 `name` 更改。
4. 当组件首次挂载时，如果存在存储的值，则使用 `Storage.getItem()` 更新 `value`，否则使用 `Storage.setItem()` 持久化当前值。
5. 当 `value` 更新时，使用 `Storage.setItem()` 存储新值。
6. 当 `name` 更新时，使用 `Storage.setItem()` 创建新键，更新 `nameRef`，并使用 `Storage.removeItem()` 从 `Window.localStorage` 中删除先前的键。
7. 请注意，该钩子适用于原始值（即非对象），并且不处理由于其他代码导致的 `Window.localStorage` 的更改。这两个问题都可以轻松处理（例如 JSON 序列化和处理 `'storage'` 事件）。

以下是代码：

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
