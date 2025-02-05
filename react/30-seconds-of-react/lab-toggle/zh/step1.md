# 切换组件

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要渲染一个切换组件，请按以下步骤操作：

1. 使用 `useState()` 钩子将 `isToggledOn` 状态变量初始化为 `defaultToggled`。
2. 渲染一个 `<input>` 元素，并绑定其 `onClick` 事件以更新 `isToggledOn` 状态变量。为包裹的 `<label>` 元素应用适当的 `className`。
3. 使用以下 CSS 为切换组件设置样式：

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

以下是代码：

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
