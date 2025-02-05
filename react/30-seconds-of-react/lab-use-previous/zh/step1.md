# React usePrevious 钩子

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要存储上一个状态或属性，你可以创建一个自定义钩子。步骤如下：

1. 定义一个接受 `value` 参数的自定义钩子。
2. 使用 `useRef()` 钩子为 `value` 创建一个 `ref`。
3. 使用 `useEffect()` 钩子记住最新的 `value`。
4. 返回 `ref.current` 的值。

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

以下是使用 `usePrevious` 钩子的示例：

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        当前值：{value} - 上一个值：{lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>增加</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

`Counter` 组件显示 `value` 的当前值和上一个值。当点击“增加”按钮时，`value` 会更新，并且上一个值会使用 `usePrevious` 钩子进行存储。

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
