# 如何在JavaScript中获取字符串的字节大小

要在JavaScript中获取字符串的字节大小，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 将字符串转换为[`Blob`对象](https://developer.mozilla.org/en-US/docs/Web/API/Blob)。
3. 使用 `Blob.size` 获取字符串的字节长度。

以下是获取字符串字节大小的JavaScript代码：

```js
const byteSize = (str) => new Blob([str]).size;
```

你可以使用以下示例测试此函数：

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
