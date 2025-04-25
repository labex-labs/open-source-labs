# 反转数字

要使用 JavaScript 反转一个数字，你可以按以下步骤使用`reverseNumber()`函数：

1. 使用`Object.prototype.toString()`将数字`n`转换为字符串。
2. 使用`String.prototype.split()`、`Array.prototype.reverse()`和`Array.prototype.join()`来获取`n`反转后的字符串值。
3. 使用`parseFloat()`将字符串转换回数字。
4. 使用`Math.sign()`保留数字的符号。

以下是`reverseNumber()`函数的代码：

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

你可以使用以下示例测试该函数：

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
