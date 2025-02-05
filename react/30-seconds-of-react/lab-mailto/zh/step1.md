# 电子邮件链接

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此函数创建一个链接，点击该链接会打开用户的电子邮件客户端，并使用指定的主题和正文内容填充一封新邮件。该链接使用 `mailto:` 协议进行格式化。

要使用此函数，请提供一个包含收件人电子邮件地址的 `email` 属性，还可选择提供 `subject` 和 `body` 属性，以便用初始内容填充邮件。在将这些属性添加到链接 URL 之前，会使用 `encodeURIComponent` 对其进行安全编码。

链接将使用提供的 `children` 作为其内容进行渲染。

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

示例用法：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
