# React 的 useComponentDidMount 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要在组件挂载后立即执行一个回调函数，你可以使用 `useEffect()` 钩子，并将空数组作为第二个参数。这将确保提供的回调函数在组件挂载时只执行一次。下面展示的 `useComponentDidMount()` 函数使用这个钩子来实现与类组件的 `componentDidMount()` 生命周期方法相同的行为。

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("组件已挂载"));

  return <div>查看控制台！</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
