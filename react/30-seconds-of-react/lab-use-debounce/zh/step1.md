# React useDebounce 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要对给定值进行防抖处理，你可以创建一个自定义钩子，它接受一个 `value` 和一个 `delay`。使用 `useState()` 钩子来存储防抖后的值，并使用 `useEffect()` 钩子在每次 `value` 更新时更新防抖后的值。为了将前一个状态变量的设置器调用延迟 `delay` 毫秒，使用 `setTimeout()`。为了在组件卸载时进行清理，使用 `clearTimeout()`。这在处理用户输入时特别有用。

以下是 `useDebounce()` 钩子的一个示例实现：

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

你可以在组件中像这样使用 `useDebounce()` 钩子：

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        当前值：{value} - 防抖后的值：{lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>增加</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
