# React 的 useComponentDidUpdate 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码提供了一个名为 `useComponentDidUpdate` 的自定义钩子，它会在组件每次更新时执行一个提供的 `callback` 函数。该钩子的执行步骤如下：

1. 使用 `useRef()` 钩子创建一个 `mounted` 变量。这个变量用于跟踪组件是否已经挂载。
2. 使用 `useEffect()` 钩子在钩子首次执行时将 `mounted` 的值设置为 `true`。
3. 在后续的钩子执行中，仅当组件已经挂载时才运行提供的 `callback` 函数。
4. 如果提供了第二个参数 `condition`，则仅当其任何依赖项发生变化时，钩子才会执行。
5. 这个钩子的行为类似于类组件的 `componentDidUpdate()` 生命周期方法。

以下是代码：

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`当前值是 ${value}。`);
  }, [value]);

  return (
    <>
      <p>
        值：{value}，另一个值：{otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>增加值</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        增加另一个值
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
