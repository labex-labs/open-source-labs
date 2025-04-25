# 将字符串转换为 URL Slug 的函数

要将字符串转换为可用于 URL 的 slug，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`String.prototype.toLowerCase()`和`String.prototype.trim()`方法规范化字符串。
3. 使用`String.prototype.replace()`方法将空格、破折号和下划线替换为`-`，并删除特殊字符。
4. 实现以下代码：

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. 使用输入`slugify('Hello World!');`测试该函数，它应返回输出`'hello-world'`。
