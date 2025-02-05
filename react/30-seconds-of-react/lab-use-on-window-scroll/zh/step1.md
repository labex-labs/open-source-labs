# React useOnWindowScroll 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此函数会在每次窗口滚动时执行一个回调函数。要实现它：

1. 使用 `useRef()` 钩子创建一个引用变量 `listener`。
2. 使用 `useEffect()` 钩子和 `EventTarget.addEventListener()` 监听 `Window` 对象的 `'scroll'` 事件，并将监听器引用赋值给 `listener.current`。
3. 当组件卸载时，使用 `EventTarget.removeEventListener()` 移除任何现有的监听器。

以下是代码：

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

要测试此函数，你可以在组件中这样使用它：

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

这将在每次窗口滚动时记录窗口的垂直滚动位置。

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
