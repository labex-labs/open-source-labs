# 汉明距离计算

要计算两个值之间的汉明距离，请遵循以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用异或运算符（`^`）找出两个数字之间的位差异。
3. 使用`Number.prototype.toString()`将结果转换为二进制字符串。
4. 使用`String.prototype.match()`计算字符串中`1`的数量。
5. 返回计数结果。

以下是`hammingDistance`函数的代码：

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

你可以通过运行`hammingDistance(2, 3); // 1`来测试该函数。
