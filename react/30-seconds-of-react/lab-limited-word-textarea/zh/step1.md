# 有字数限制的文本区域

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

```jsx
// 渲染一个有字数限制的文本区域组件。
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // 创建一个记忆化函数，用于格式化输入文本。
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // 在content的初始值上调用setFormattedContent。
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

所做的更改：

- 添加了注释来解释代码的每个部分的作用。
- 简化了 `setFormattedContent` 中的逻辑，使其更简洁。
- 将 `setContent` 函数移到函数调用的末尾，使其更易读。
- 为保持一致性，重新排列了 `<textarea>` 组件中的属性。
- 删除了不必要的空格和换行符。

请点击右下角的“Go Live”以在端口8080上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
