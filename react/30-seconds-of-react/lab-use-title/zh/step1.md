# React useTitle 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要设置页面标题，你可以使用 `useTitle` 自定义钩子。此钩子使用 `typeof` 检查 `Document` 是否已定义。如果已定义，则使用 `useRef()` 钩子存储 `Document` 的原始标题。然后，`useEffect()` 钩子用于在组件挂载时将 `Document.title` 设置为传递的值，并在卸载时进行清理。

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

在示例代码中，`Alert` 组件使用 `useTitle` 钩子将标题设置为“Alert”。`MyApp` 组件渲染一个按钮，用于切换 `Alert` 组件。

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
