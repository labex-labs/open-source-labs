# 不受控文本区域元素

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此函数会渲染一个不受父组件控制的 `<textarea>` 元素。它使用一个回调函数将输入的值传递给父组件。

要使用此函数：

- 从父组件传递 `defaultValue` 属性作为输入字段的初始值。
- 使用 `onChange` 事件触发 `onValueChange` 回调，并将新值发送给父组件。

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

示例用法：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
