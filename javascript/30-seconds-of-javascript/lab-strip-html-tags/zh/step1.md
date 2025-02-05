# 如何从字符串中移除 HTML/XML 标签

要从字符串中移除 HTML/XML 标签，你可以使用正则表达式。请按以下步骤操作：

1. 打开终端/SSH
2. 输入 `node` 以开始练习编码
3. 使用以下代码：

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. 使用以下示例测试该函数：

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

这将从输入字符串中移除所有 HTML/XML 标签，并返回剩余的文本。
