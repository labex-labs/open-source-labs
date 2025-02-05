# React useBodyScrollLock 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码片段允许用户在模态框打开时锁定页面主体滚动。其工作原理如下：

首先，定义了 `useBodyScrollLock` 函数，该函数使用 `useLayoutEffect` 钩子来锁定 `body` 元素的滚动。这个钩子在组件挂载时只运行一次，它将 `body` 元素的 `overflow` 值设置为 `'hidden'`。当组件卸载时，恢复原来的 `overflow` 值。

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

然后，定义了 `Modal` 组件，它使用了 `useBodyScrollLock` 函数。这个组件在屏幕中央的一个框中显示一条消息。当点击这个框时，模态框关闭，页面主体滚动解锁。

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        滚动已锁定！ <br /> 点击此处解锁
      </p>
    </div>
  );
};
```

最后，定义了 `MyApp` 组件，它渲染一个按钮，点击该按钮时会打开 `Modal` 组件。

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>打开模态框</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
