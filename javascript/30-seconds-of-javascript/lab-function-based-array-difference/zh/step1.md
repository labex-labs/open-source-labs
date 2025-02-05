# 如何根据函数从数组中过滤值

要根据给定的比较函数从数组中过滤出所有值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.filter()` 和 `Array.prototype.findIndex()` 找到合适的值。
3. 省略最后一个参数 `comp`，以使用默认的严格相等比较器。
4. 使用以下代码：

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. 使用以下示例测试你的函数：

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // 预期输出：[1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // 预期输出：[1.2]
```
