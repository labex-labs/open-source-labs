# 如何在 JavaScript 中生成随机字母数字字符串

要在 JavaScript 中生成随机字母数字字符的字符串，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.from()` 创建一个指定长度的新数组。
3. 使用 `Math.random()` 生成一个随机浮点数。
4. 使用 `Number.prototype.toString()` 将数字转换为基数为 `36` 的字母数字字符串。
5. 使用 `String.prototype.slice()` 从每个生成的数字中删除整数部分和小数点。
6. 使用 `Array.prototype.some()` 根据需要重复此过程多次，直到达到 `length`，因为它每次都会生成一个可变长度的字符串。
7. 如果生成的字符串比给定的 `length` 长，则使用 `String.prototype.slice()` 缩短它。
8. 返回生成的字符串。

以下是代码：

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

你可以将所需的长度作为参数调用 `randomAlphaNumeric()` 函数。例如：

```js
randomAlphaNumeric(5); // '0afad'
```
