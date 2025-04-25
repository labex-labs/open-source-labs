# React useError 钩子

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码创建了一个错误调度器。它使用三个 React 钩子来管理错误状态并将其分派到用户界面。

代码的工作原理如下：

1. `useState()` 钩子创建一个名为 `error` 的状态变量，用于保存错误对象。它接受一个初始值 `err`，该值作为参数传递给钩子。

2. `useEffect()` 钩子用于在错误为真值时“抛出”错误。这个钩子接受一个函数和一个依赖项数组作为参数。在这种情况下，函数会检查 `error` 状态变量是否为真值（即不为 null、undefined、0、false 或空字符串），如果是则抛出它。依赖项数组是 `[error]`，这意味着每当 `error` 变量发生变化时，该副作用都会重新运行。

3. `useCallback()` 钩子用于创建一个名为 `dispatchError` 的缓存函数，该函数更新 `error` 状态变量并返回新函数。这个钩子接受一个函数和一个依赖项数组作为参数。在这种情况下，函数接受一个参数 `err`，它是要分派的新错误对象。依赖项数组是 `[]`，这意味着只有在组件重新渲染时才会重新创建缓存函数。

以下是在组件中使用 `useError()` 钩子的示例：

1. 创建一个名为 `ErrorButton` 的新组件。

2. 在组件内部，调用 `useError()` 钩子以获取 `dispatchError` 函数。

3. 创建一个名为 `clickHandler` 的点击处理函数，该函数使用新的错误对象调用 `dispatchError`。

4. 渲染一个按钮，点击时调用 `clickHandler`。

以下是代码：

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
