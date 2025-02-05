# React useLocalStorage 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

此函数创建一个保存到 `localStorage` 的值以及一个用于修改它的函数。其工作原理如下：

1. 要创建该值，使用 `useState()` 钩子并传入一个函数来延迟初始化它。
2. 要从 `localStorage` 中检索保存的值，使用 `try...catch` 块和 `Storage.getItem()`。如果没有保存的值，则使用 `Storage.setItem()` 存储 `defaultValue` 并将其用作初始状态。如果出现错误，则使用 `defaultValue`。
3. 定义一个函数，该函数使用传入的值更新状态变量，并使用 `Storage.setItem()` 保存它。

以下是代码：

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

你可以在应用中这样使用此函数：

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
