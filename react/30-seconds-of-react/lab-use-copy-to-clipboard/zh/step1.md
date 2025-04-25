# React useCopyToClipboard 钩子

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要将给定文本复制到剪贴板，请使用 `/js/s/copy-to-clipboard/` 中提供的 `copyToClipboard` 代码片段以及 `useState()` 钩子来初始化 `copied` 变量。要为 `copyToClipboard` 方法创建一个回调函数，请使用 `useCallback()` 钩子。要在 `text` 发生变化时重置 `copied` 状态变量，请使用 `useEffect()` 钩子。最后，返回 `copied` 状态变量和 `copy` 回调函数。

以下代码展示了一个如何使用这些钩子和方法来创建 `TextCopy` 组件的示例。当用户点击“点击复制”按钮时，会调用 `copy` 函数，并且 `copied` 变量会被设置为 `true`。如果复制成功，将会显示“已复制！”。

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
