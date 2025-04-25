# 查找数组的第 N 个元素

要查找数组的第 n 个元素，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.slice()` 创建一个包含第 n 个元素的新数组。
3. 如果索引越界，则返回 `undefined`。
4. 省略第二个参数 `n` 以获取数组的第一个元素。

以下是实现此功能的示例代码：

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

你可以使用以下示例测试此函数：

```js
nthElement(["a", "b", "c"], 1); // 输出：'b'
nthElement(["a", "b", "b"], -3); // 输出：'a'
```

按照这些步骤，你可以使用 JavaScript 轻松找到数组的第 n 个元素。
