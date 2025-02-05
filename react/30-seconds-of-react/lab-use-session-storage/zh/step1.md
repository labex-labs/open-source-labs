# React useSessionStorage 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要创建一个持久化到 `sessionStorage` 的有状态值以及一个更新它的函数，请执行以下步骤：

1. 使用 `useState()` 钩子并传入一个函数来延迟初始化其值。
2. 使用 `try...catch` 块和 `Storage.getItem()` 尝试从 `Window.sessionStorage` 获取值。如果未找到值，则使用 `Storage.setItem()` 存储 `defaultValue` 并将其用作初始状态。如果发生错误，则使用 `defaultValue` 作为初始状态。
3. 定义一个函数，该函数将使用传入的值更新状态变量，并使用 `Storage.setItem()` 存储它。

以下是一个示例实现：

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

你可以在应用中这样使用这个钩子：

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
