# 如何在JavaScript中填充数字

要在JavaScript中填充数字，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 在将数字转换为字符串后，使用 `String.prototype.padStart()` 方法将数字填充到指定长度。
3. 下面的 `padNumber()` 函数演示了这种方法。
4. 将数字和所需长度作为参数传递给函数。
5. 该函数返回填充后的数字作为字符串。

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

示例用法：

```js
padNumber(1234, 6); // '001234'
```
