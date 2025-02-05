# 显示/隐藏密码切换

> VM 中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

以下代码呈现了一个带有显示按钮的密码输入字段。它使用 `useState()` 钩子创建 `shown` 状态变量，并将其初始值设置为 `false`。当点击“显示/隐藏”按钮时，会调用 `setShown` 函数，在 `'text'` 和 `'password'` 之间切换输入的 `type`。

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
