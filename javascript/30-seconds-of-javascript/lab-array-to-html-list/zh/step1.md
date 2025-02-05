# 将数组转换为 HTML 列表

要开始编码，请启动终端/SSH 并输入 `node`。

此函数将给定的数组元素转换为 `<li>` 标签，并将它们添加到具有给定 id 的列表中。

使用 `Array.prototype.map()` 和 `Document.querySelector()` 生成 HTML 标签列表。

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

示例用法：

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
