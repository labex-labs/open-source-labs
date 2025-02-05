# 对 HTML 进行转义

此函数用于对转义后的 HTML 字符进行反转义。使用步骤如下：

1. 打开终端/SSH。
2. 输入 `node`。
3. 复制并粘贴以下代码：

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"'
      })[tag] || tag
  );
```

4. 调用 `unescapeHTML` 函数，并向其传递一个包含转义字符的字符串。
5. 该函数将返回反转义后的字符串。

示例用法：

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
