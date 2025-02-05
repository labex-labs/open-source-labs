# 不受控输入字段

> VM 中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码渲染了一个不受控的 `<input>` 元素，它使用回调函数将值更新通知给其父组件。使用方法如下：

- 使用 `defaultValue` 属性从父组件传递初始值。
- 传递一个名为 `onValueChange` 的回调函数来处理值更新。
- 使用 `onChange` 事件触发回调并将新值发送给父组件。

以下是一个示例：

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
