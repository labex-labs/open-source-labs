# React useSearchParam 钩子

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要跟踪浏览器的位置搜索参数，请执行以下步骤：

1. 使用 `useCallback()` 钩子创建一个回调函数。该回调函数应使用 `URLSearchParams` 构造函数来获取所需参数的当前值。

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. 使用 `useState()` 钩子创建一个状态变量，用于保存参数的当前值。

```jsx
const [value, setValue] = React.useState(getValue);
```

3. 使用 `useEffect()` 钩子设置适当的事件监听器，以便在挂载时更新状态变量，并在卸载时清理它们。

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

以下是在组件中使用此自定义钩子的示例：

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Post 参数值：{post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        查看帖子 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        退出
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

此示例创建了一个 `MyApp` 组件，该组件使用 `useSearchParam` 自定义钩子来跟踪位置搜索中 `post` 参数的值。`post` 值显示在一个段落标签中。还包含两个按钮，用于演示如何更改位置搜索参数值。

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页以预览网页。
