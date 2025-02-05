# React useKeyPress 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此函数监听给定按键按下状态的变化。使用方法如下：

- 以目标按键作为参数调用 `useKeyPress()`。
- `useKeyPress()` 返回一个布尔值，指示该按键当前是否被按下。
- 该函数使用 `useState()` 钩子创建一个状态变量，用于保存给定按键的按下状态。
- 它定义了两个处理函数，分别在按键按下或松开时更新状态变量。
- `useEffect()` 钩子和 `EventTarget.addEventListener()` 用于处理 `'keydown'` 和 `'keyup'` 事件。
- 最后，`EventTarget.removeEventListener()` 用于在组件卸载后执行清理操作。

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

以下是 `useKeyPress()` 在 React 组件中的一个使用示例：

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
