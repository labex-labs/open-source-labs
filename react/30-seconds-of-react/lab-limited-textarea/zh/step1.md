# 有字符限制的文本区域

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

以下是代码：

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

在这段代码中，我们：

- 简化了注释，以便更简洁地概述代码各部分的功能。
- 删除了不必要的代码注释。
- 从 `useCallback` 的依赖数组中移除了 `setContent` 函数，因为它不需要在那里。
- 在 `useCallback` 函数的 `text` 参数周围添加了括号，以保持一致性。
- 为简洁起见，对 `onChange` 事件处理程序使用了箭头函数。

请点击右下角的“Go Live”在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
