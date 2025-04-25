# 检查字符串中的空白字符

要检查字符串是否包含空白字符，请按照以下步骤操作：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `RegExp.prototype.test()` 和适当的正则表达式来检查给定字符串是否包含任何空白字符。
- 以下是一个示例代码片段：

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- 要测试该函数，请将字符串作为参数调用 `containsWhitespace`。如果字符串包含空白字符，它将返回 `true`，否则返回 `false`。

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
