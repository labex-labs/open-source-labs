# 如何在 JavaScript 中移除非 ASCII 字符

要在 JavaScript 中移除不可打印的 ASCII 字符，你可以遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.replace()` 方法和正则表达式来移除不可打印的 ASCII 字符。
3. 正则表达式 `/[^\x20-\x7E]/g` 匹配任何不在可打印 ASCII 范围内的字符（十进制值 32 到 126）。
4. `g` 标志用于执行全局匹配（即替换字符串中所有非 ASCII 字符的出现）。
5. 以下是如何使用 `removeNonASCII` 函数的示例：

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

这将返回移除了所有非 ASCII 字符的字符串。
