# React 的 useComponentWillUnmount 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要在组件卸载和销毁之前立即执行一个回调函数，你可以使用 `useEffect()` 钩子，并将空数组作为第二个参数。返回提供的回调函数，使其仅在清理之前执行一次。这种行为类似于类组件的 `componentWillUnmount()` 生命周期方法。你也可以使用以下代码片段创建一个自定义钩子 `useComponentWillUnmount()`，它接受一个 `onUnmountHandler` 函数作为参数，并在组件卸载之前执行它：

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

然后，你可以在函数式组件中像这样使用这个自定义钩子：

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

当组件即将卸载时，这将在控制台中输出 "Component will unmount"。

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
