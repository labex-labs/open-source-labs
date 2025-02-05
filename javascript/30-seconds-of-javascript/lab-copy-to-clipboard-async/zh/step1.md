# 将字符串复制到剪贴板的函数

要将字符串复制到剪贴板，请使用 `copyToClipboardAsync` 函数。该函数返回一个 Promise，当剪贴板内容更新时它会被 resolve。以下是步骤：

1. 通过使用 `if` 语句检查 `Navigator`、`Navigator.clipboard` 和 `Navigator.clipboard.writeText` 是否为真值，来判断剪贴板 API 是否可用。
2. 如果剪贴板 API 可用，使用 `Clipboard.writeText()` 将给定的值 `str` 写入剪贴板。
3. 返回 `Clipboard.writeText()` 的结果，这是一个 Promise，当剪贴板内容更新时它会被 resolve。
4. 如果剪贴板 API 不可用，使用 `Promise.reject()` 以适当的错误消息拒绝该 Promise。
5. 如果你需要支持旧版浏览器，请使用 `Document.execCommand()` 代替 `Clipboard.writeText()`。你可以在 `copyToClipboard` 代码片段中了解更多相关信息。

以下是 `copyToClipboardAsync` 函数：

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

要使用该函数，将你想要复制的字符串作为参数调用 `copyToClipboardAsync`，如下所示：

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' 已复制到剪贴板。
```
