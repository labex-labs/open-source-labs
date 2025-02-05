# React 的 useMutationObserver 钩子

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要监听对 DOM 树所做的更改，可以使用 `useMutationObserver` 钩子。其工作原理如下：

1. 该钩子接受三个参数：`ref`、`callback` 和 `options`。
2. 在钩子内部，使用了一个依赖于 `callback` 和 `options` 值的 `useEffect()` 钩子。
3. 如果给定的 `ref` 已初始化，则创建一个新的 `MutationObserver` 并将 `callback` 传递给它。
4. 使用给定的 `options` 调用 `MutationObserver.observe()` 来监听给定的 `ref` 的变化。
5. 当组件卸载时，使用 `MutationObserver.disconnect()` 从 `ref` 中移除观察者。

以下是代码：

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

在 `App` 组件中，使用 `useMutationObserver` 钩子来监听对 `mutationRef` 元素所做的更改。`incrementMutationCount` 函数作为 `callback` 传递。

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">编辑此内容以更新文本：</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>调整大小或更改内容：</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>变化计数 {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
