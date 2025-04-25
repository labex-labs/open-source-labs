# 不受控范围输入

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要在 React 中创建滑块，请使用 `Slider` 组件并传入 `min`、`max`、`defaultValue` 和 `onValueChange` 属性。

在 `Slider` 组件中，将 `<input>` 元素的 `type` 设置为 `"range"` 以创建滑块。使用从父组件传递下来的 `defaultValue` 属性作为不受控输入字段的初始值。使用 `onChange` 事件触发 `onValueChange` 回调，并将新值发送给父组件。

以下是 `Slider` 组件的代码：

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

要渲染 `Slider` 组件，请使用 `ReactDOM.createRoot` 并传入 `onValueChange` 回调函数：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页以预览网页。
