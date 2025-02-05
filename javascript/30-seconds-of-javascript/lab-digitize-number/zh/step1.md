# 如何将数字数位化

要在 JavaScript 中将数字数位化，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Math.abs()` 去掉数字的符号。
3. 将数字转换为字符串，并使用展开运算符（`...`）创建一个由各个数位组成的数组。
4. 使用 `Array.prototype.map()` 和 `parseInt()` 将每个数位转换为整数。

以下是 `digitize` 函数的代码：

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

示例用法：

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
