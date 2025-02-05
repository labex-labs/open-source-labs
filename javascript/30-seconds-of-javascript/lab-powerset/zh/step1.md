# 如何在JavaScript中生成幂集

要在JavaScript中生成给定数字数组的幂集，请遵循以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduce()` 方法结合 `Array.prototype.map()` 方法来遍历元素，并将它们组合成一个包含所有组合的数组。
3. 实现以下代码：

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. 要生成幂集，调用函数 `powerset()` 并将数组作为参数传入。例如：

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

这将返回一个包含给定数组所有可能子集的数组。
