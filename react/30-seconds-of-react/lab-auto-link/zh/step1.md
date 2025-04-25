# 自动文本链接

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这个组件将字符串渲染为纯文本，同时将 URL 转换为适当的链接元素。

为了实现这一点，它使用 `String.prototype.split()` 和 `String.prototype.match()` 以及一个正则表达式在给定字符串中查找 URL。然后，匹配到的 URL 将作为 `<a>` 元素返回，必要时会处理缺失的协议前缀。字符串的其余部分将渲染为纯文本。

以下是代码：

```jsx
const AutoLink = ({ text }) => {
  const urlRegex =
    /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;

  const renderText = () => {
    return text.split(urlRegex).map((word, index) => {
      const urlMatch = word.match(urlRegex);
      if (urlMatch) {
        const url = urlMatch[0];
        return (
          <a key={index} href={url.startsWith("http") ? url : `http://${url}`}>
            {url}
          </a>
        );
      }
      return <span key={index}>{word}</span>;
    });
  };

  return <div>{renderText()}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <AutoLink text="foo bar baz http://example.org bar" />
);
```

请点击右下角的“Go Live”在 8080 端口运行 Web 服务。然后，你可以刷新**Web 8080**标签页来预览网页。
