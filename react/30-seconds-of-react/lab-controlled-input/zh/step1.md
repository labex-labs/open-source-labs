# 受控输入字段

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此代码片段提供了一个受控的 `<input>` 元素，它使用回调函数将其值的任何更新通知给父元素。其工作原理如下：

- 受控输入字段的值由父元素传递下来的 `value` 属性决定。
- 用户对输入字段所做的任何更改都会被 `onChange` 事件捕获，该事件会触发 `onValueChange` 回调函数，并将新值发送回父组件。
- 要更新输入字段的值，父元素必须更新传递给受控输入组件的 `value` 属性。

以下是 `ControlledInput` 组件的示例实现，后面跟着 `Form` 组件中的使用示例：

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Insert some text here..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
